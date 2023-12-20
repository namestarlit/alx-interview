## 0x03. Log Parsing
### Script for Computing Metrics from stdin

This script reads stdin line by line and computes metrics based on the provided input format:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
  - If the format is not as specified, the line is skipped.

After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints the following statistics from the beginning:

- **Total file size:** `File size: <total size>`
  - Where `<total size>` is the sum of all previous `<file size>` (as per the input format).

- **Number of lines by status code:**
  - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.
  - If a status code doesn’t appear or is not an integer, the script does not print anything for that status code.
  - Format: `<status code>: <number>`
  - Status codes are printed in ascending order.

**Warning:** The output may vary with random values; it's normal to not have the same output as the provided sample.


