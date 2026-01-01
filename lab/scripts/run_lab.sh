diff --git a/lab/scripts/run_lab.sh b/lab/scripts/run_lab.sh
new file mode 100755
index 0000000000000000000000000000000000000000..7ce072adbc26330ed4f6d6e2af98e3984b1ca92a
--- /dev/null
+++ b/lab/scripts/run_lab.sh
@@ -0,0 +1,13 @@
+#!/usr/bin/env bash
+set -euo pipefail
+
+EML_PATH=${1:-lab/sample/phishing_sample.eml}
+REPORT_PATH=${2:-lab/output/analysis_report.md}
+
+python3 lab/scripts/parse_eml.py "$EML_PATH" --output "$REPORT_PATH"
+
+echo ""
+python3 lab/scripts/extract_attachments.py "$EML_PATH" --output lab/output --report "$REPORT_PATH"
+
+echo ""
+echo "Report saved to $REPORT_PATH"
