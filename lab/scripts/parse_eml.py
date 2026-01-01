diff --git a/lab/scripts/parse_eml.py b/lab/scripts/parse_eml.py
new file mode 100755
index 0000000000000000000000000000000000000000..8329c19dc349a358f3c55cad304685a2400910d3
--- /dev/null
+++ b/lab/scripts/parse_eml.py
@@ -0,0 +1,72 @@
+#!/usr/bin/env python3
+"""Parse an EML file and print key phishing analysis indicators."""
+from __future__ import annotations
+
+import argparse
+import re
+from email import policy
+from email.parser import BytesParser
+from pathlib import Path
+
+URL_RE = re.compile(r"https?://[^\s'\"]+")
+
+
+def extract_urls(text: str) -> list[str]:
+    return URL_RE.findall(text or "")
+
+
+def build_report(message) -> str:
+    lines: list[str] = []
+    lines.append("== Header Summary ==")
+    for header in ("From", "To", "Subject", "Date", "Message-ID"):
+        lines.append(f"{header}: {message.get(header)}")
+
+    lines.append("\n== Authentication Results ==")
+    auth_results = message.get_all("Authentication-Results", [])
+    if auth_results:
+        lines.extend(auth_results)
+    else:
+        lines.append("No Authentication-Results header found.")
+
+    lines.append("\n== Received Chain ==")
+    received_headers = message.get_all("Received", [])
+    if received_headers:
+        lines.extend(received_headers)
+    else:
+        lines.append("No Received headers found.")
+
+    lines.append("\n== URLs Found ==")
+    urls: list[str] = []
+    for part in message.walk():
+        if part.get_content_maintype() == "multipart":
+            continue
+        if part.get_content_type() in {"text/plain", "text/html"}:
+            payload = part.get_content()
+            urls.extend(extract_urls(payload))
+    if urls:
+        for url in sorted(set(urls)):
+            lines.append(url)
+    else:
+        lines.append("No URLs found.")
+
+    return "\n".join(lines)
+
+
+def main() -> None:
+    parser = argparse.ArgumentParser(description="Parse an EML file for analysis.")
+    parser.add_argument("eml", type=Path, help="Path to .eml file")
+    parser.add_argument("--output", type=Path, help="Write summary to a file")
+    args = parser.parse_args()
+
+    message = BytesParser(policy=policy.default).parsebytes(args.eml.read_bytes())
+
+    report = build_report(message)
+    print(report)
+
+    if args.output:
+        args.output.parent.mkdir(parents=True, exist_ok=True)
+        args.output.write_text(report + "\n", encoding="utf-8")
+
+
+if __name__ == "__main__":
+    main()
