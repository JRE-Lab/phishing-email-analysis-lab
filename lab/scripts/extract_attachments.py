diff --git a/lab/scripts/extract_attachments.py b/lab/scripts/extract_attachments.py
new file mode 100755
index 0000000000000000000000000000000000000000..84d95e5712265c4c4fa76bb2b21e29aa07aed444
--- /dev/null
+++ b/lab/scripts/extract_attachments.py
@@ -0,0 +1,64 @@
+#!/usr/bin/env python3
+"""Extract attachments from an EML file and compute hashes."""
+from __future__ import annotations
+
+import argparse
+import hashlib
+from email import policy
+from email.parser import BytesParser
+from pathlib import Path
+
+
+def sha256_file(path: Path) -> str:
+    digest = hashlib.sha256()
+    with path.open("rb") as handle:
+        for chunk in iter(lambda: handle.read(8192), b""):
+            digest.update(chunk)
+    return digest.hexdigest()
+
+
+def main() -> None:
+    parser = argparse.ArgumentParser(description="Extract attachments from an EML file.")
+    parser.add_argument("eml", type=Path, help="Path to .eml file")
+    parser.add_argument("--output", type=Path, default=Path("lab/output"), help="Output directory")
+    parser.add_argument("--report", type=Path, help="Append attachment summary to report file")
+    args = parser.parse_args()
+
+    args.output.mkdir(parents=True, exist_ok=True)
+
+    message = BytesParser(policy=policy.default).parsebytes(args.eml.read_bytes())
+
+    attachments = []
+    for part in message.iter_attachments():
+        filename = part.get_filename() or "attachment.bin"
+        out_path = args.output / filename
+        out_path.write_bytes(part.get_payload(decode=True))
+        attachments.append(out_path)
+
+    if not attachments:
+        message = "No attachments found."
+        print(message)
+        if args.report:
+            args.report.parent.mkdir(parents=True, exist_ok=True)
+            with args.report.open("a", encoding="utf-8") as handle:
+                handle.write("\n== Attachment Summary ==\n")
+                handle.write(message + "\n")
+        return
+
+    lines = ["Saved attachments:"]
+    for attachment in attachments:
+        lines.append(f"- {attachment} (sha256={sha256_file(attachment)})")
+
+    output = "\n".join(lines)
+    print(output)
+
+    if args.report:
+        args.report.parent.mkdir(parents=True, exist_ok=True)
+        with args.report.open("a", encoding="utf-8") as handle:
+            handle.write("\n== Attachment Summary ==\n")
+            handle.write(output)
+            handle.write("\n")
+
+
+if __name__ == "__main__":
+    main()
