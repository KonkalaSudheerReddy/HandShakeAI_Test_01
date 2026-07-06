Analyze `/app/access.log` and save the results as a valid JSON object in
`/app/report.json`.

The JSON object must contain these three fields:

- `total_requests`: the number of non-empty request lines in the access log.
- `unique_ips`: the number of distinct client IP addresses, using the first
  whitespace-delimited value on each request line as the client IP address.
- `top_path`: the request path that occurs most often, using the value between the
  HTTP method and HTTP protocol on each request line.

These are the only required findings. Additional JSON fields are allowed.
