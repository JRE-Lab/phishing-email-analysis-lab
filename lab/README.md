diff --git a/lab/README.md b/lab/README.md
new file mode 100644
index 0000000000000000000000000000000000000000..06350e61050967cbf70136d8f363b1294905b1fd
--- /dev/null
+++ b/lab/README.md
@@ -0,0 +1,88 @@
+# Phishing Email Analysis Lab (Hands-On)
+
+This lab walks you through a safe, offline phishing analysis exercise using a **sample email** and **local tooling**. You will inspect headers, identify social engineering cues, extract attachments safely, and document indicators of compromise (IOCs).
+
+> ⚠️ **Safety Reminder**: Do **not** click links or open attachments directly from an email client. Use the scripts in this lab or a dedicated analysis VM.
+
+## What’s Included
+
+```
+lab/
+├── README.md                  # This guide
+├── ioc_template.md            # IOC/analysis worksheet
+├── sample/
+│   ├── phishing_sample.eml    # Sample phishing email
+│   └── Invoice_2024.txt        # Safe attachment (training only)
+├── scripts/
+│   ├── parse_eml.py            # Header + URL extraction
+│   ├── extract_attachments.py  # Safe attachment extraction + hashes
+│   └── run_lab.sh              # Convenience wrapper
+└── output/                     # Extracted attachments + report (created during lab)
+```
+
+## Prerequisites
+
+- Python 3.8+ (no external packages required)
+- Optional: Linux VM for extra isolation
+
+## Quick Start
+
+**Recommended (wrapper script):**
+
+```bash
+./lab/scripts/run_lab.sh
+```
+
+**Manual commands:**
+
+```bash
+python3 lab/scripts/parse_eml.py lab/sample/phishing_sample.eml --output lab/output/analysis_report.md
+python3 lab/scripts/extract_attachments.py lab/sample/phishing_sample.eml --output lab/output --report lab/output/analysis_report.md
+```
+
+The combined report is saved to `lab/output/analysis_report.md`.
+
+## Lab Steps
+
+### 1) Review Email Headers
+
+Inspect the output for:
+
+- Lookalike or misspelled sender domains
+- Authentication failures (SPF/DKIM/DMARC)
+- Suspicious hops in the `Received` chain (private IPs, odd relays)
+
+### 2) Inspect the Email Body
+
+Look for:
+
+- Urgency or threats (e.g., “verify within 24 hours”)
+- Mismatched link text and destination domains
+- Poor grammar or inconsistent branding
+
+### 3) Extract and Hash Attachments
+
+Use `extract_attachments.py` (or the wrapper) to extract attachments without opening them. Record SHA-256 hashes for IOC tracking.
+
+### 4) Document Indicators of Compromise
+
+Use `lab/ioc_template.md` to capture:
+
+- Sender domains and IPs
+- URLs/domains from the body
+- Attachment hashes
+- Suspicious subjects or message IDs
+
+## Success Criteria
+
+By the end of the lab, you should be able to:
+
+- Explain why the email is suspicious
+- List key IOCs
+- Demonstrate safe handling of email artifacts
+
+## Optional Extensions
+
+- Import the `.eml` file into a sandboxed mail client and compare findings
+- Run `whois` or `dig` on domains in the email (inside a VM)
+- Convert findings into SIEM detections or alert rules
