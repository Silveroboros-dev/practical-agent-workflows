# Focused measurements

## HTTP phases

For an authorized curl probe, use separate files for the response body,
response headers, stderr and selected write-out metrics. Capture the shell
exit code as well as the HTTP code. Avoid unrestricted verbose output for
authenticated or signed requests.

Useful fields: `time_namelookup`, `time_connect`, `time_appconnect`,
`time_starttransfer`, `time_total`, `response_code`, `size_download`,
`remote_ip` and `num_connects`. Confirm support in the installed curl version.
These phase times are cumulative; redirects, connection reuse and proxies
affect interpretation. A zero field alone is not proof of a failed phase.

`--connect-timeout` bounds connection setup, including DNS and TLS;
`--max-time` bounds the entire transfer. Exit 28 means a timeout condition,
not a specific failed layer. Avoid implicit retries in a counted probe.
An HTTP error can still accompany a successful transfer exit unless HTTP
failure handling was requested. HEAD and GET may behave differently.

Source: [curl manual](https://curl.se/docs/manpage.html), especially write-out,
connect-timeout, max-time, exit codes and fail options.

## Object store / Parquet

When a reader reports inconsistent byte-range lengths or decoded row counts,
preserve the complete sanitized error and inspect source matching the installed
reader version. Do not infer the meaning of `left` and `right` from numbers.

The cheapest useful next capture usually isolates a failing object and its
identity, rather than rerunning a whole corpus query. Within the authorized
read scope, collect request range, response status, `Content-Range`,
`Content-Length`, bytes received, ETag/version and relevant footer/schema
metadata. Signed query strings and storage credentials stay out of the report.

Azure supports conditional reads using ETags, and range semantics can return
fewer bytes at the end of an object. These facts motivate a consistency check;
they do not prove that a particular object was modified or truncated.

Sources: [Azure range headers](https://learn.microsoft.com/en-us/rest/api/storageservices/specifying-the-range-header-for-blob-service-operations)
and [Azure conditional headers](https://learn.microsoft.com/en-us/rest/api/storageservices/specifying-conditional-headers-for-blob-service-operations).

If the same fixed bytes fail offline, investigate file/decoder compatibility.
If bytes or ETags differ, establish why before changing retries. If the failing
object cannot yet be identified, prepare narrowly scoped instrumentation first;
do not assume that an arbitrary sample proves the failed full scan repaired.
