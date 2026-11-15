import importlib.util
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
spec = importlib.util.spec_from_file_location('reading_renderer', SCRIPTS / 'render_md_html.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.hrefs.append(dict(attrs).get('href'))


class HelperTests(unittest.TestCase):
    def test_unclosed_fence_preserves_code(self):
        body, _ = renderer.markdown_body('# Example\n\n```text\nKEEP_THIS <value>\n')
        self.assertIn('KEEP_THIS &lt;value&gt;', body)
        self.assertIn('<pre', body)

    def test_link_query_is_not_double_escaped(self):
        parsed = Links()
        parsed.feed(renderer.inline('[Search](https://example.test/?a=1&b=2)'))
        self.assertEqual(parsed.hrefs, ['https://example.test/?a=1&b=2'])

    def test_active_link_schemes_are_plain_text(self):
        for destination in ['javascript:run', 'data:text/html,hello', 'vbscript:run', 'java\tscript:run']:
            with self.subTest(destination=destination):
                rendered = renderer.inline('[Label](' + destination + ')')
                parsed = Links()
                parsed.feed(rendered)
                self.assertFalse(parsed.hrefs)
                self.assertIn('Label', rendered)

    def test_heading_inside_code_is_not_a_document_heading(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = root / 'source.md'
            output = root / 'output.html'
            source.write_text('# Title\n\n## Body\n\n```text\n## Code example\n```\n')
            renderer.render(source, output, 'dark')
            result = subprocess.run([sys.executable, str(SCRIPTS / 'validate_html_doc.py'), str(source), str(output)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_portal_links_existing_documents(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ['dark.html', 'light.html']:
                (root / name).write_text('<html><body>Fixture</body></html>')
            result = subprocess.run([sys.executable, str(SCRIPTS / 'build_docs_portal.py'), '--out', str(root), '--doc', 'Fixture|Example|dark.html|light.html'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            parsed = Links()
            parsed.feed((root / 'index.html').read_text())
            self.assertEqual(set(parsed.hrefs), {'dark.html', 'light.html'})
            self.assertTrue(all((root / p).is_file() for p in parsed.hrefs))

    def test_portal_rejects_missing_escaping_or_executable_links(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'light.html').write_text('fixture')
            for dark in ['missing.html', '../outside.html', 'javascript:run', 'https://example.test/page.html']:
                with self.subTest(dark=dark):
                    result = subprocess.run([sys.executable, str(SCRIPTS / 'build_docs_portal.py'), '--out', str(root), '--doc', 'Fixture|Example|' + dark + '|light.html'], capture_output=True, text=True)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertFalse((root / 'index.html').exists())


if __name__ == '__main__':
    unittest.main()
