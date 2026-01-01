diff --git a/lab/README.md b/lab/README.md
new file mode 100644
index 0000000000000000000000000000000000000000..74870682ed9aee256a2c6bc54efbe7669fa010ee
--- /dev/null
+++ b/lab/README.md
@@ -0,0 +1,84 @@
+# Phishing Email Analysis Lab (Hands-On)
+
+This lab provides a safe, self-contained phishing analysis exercise using a **sample email** and **offline tooling**. The goal is to inspect headers, identify social engineering indicators, extract attachments safely, and document indicators of compromise (IOCs).
+
+> ⚠️ **Safety**: Do **not** click links or open attachments directly from an email client. Use the provided scripts or a dedicated analysis VM.
+
+## Contents
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
+└── output/                     # Extracted attachments (created during lab)
+```
+
+## Prerequisites
+
+* Python 3.8+ (no external packages required)
+* (Optional) A Linux VM for extra isolation
+
+## Quick Start (CLI)
+
+```bash
+python3 lab/scripts/parse_eml.py lab/sample/phishing_sample.eml --output lab/output/analysis_report.md
+python3 lab/scripts/extract_attachments.py lab/sample/phishing_sample.eml --output lab/output --report lab/output/analysis_report.md
+```
+
+Or run the wrapper (recommended):
+
+```bash
+./lab/scripts/run_lab.sh
+```
+
+## Step-by-Step Lab
+
+### 1) Review the Email Headers
+
+Run `parse_eml.py` and look for:
+
+* **From** domain mismatches (typos, lookalike domains)
+* **Authentication-Results** failures (SPF/DKIM/DMARC)
+* **Received** chain anomalies (private IPs, suspicious relays)
+
+### 2) Inspect the Email Body
+
+Identify:
+
+* Urgency or fear tactics ("verify within 24 hours")
+* Links that **look** legitimate but resolve to different domains
+* Poor grammar or inconsistent branding
+
+### 3) Extract and Hash Attachments
+
+Use `extract_attachments.py` to extract attachments without opening them. Capture the SHA-256 hash for IOC tracking. The wrapper writes a combined report to `lab/output/analysis_report.md`.
+
+### 4) Document Indicators of Compromise
+
+Use `lab/ioc_template.md` to record:
+
+* Sender domains and IPs
+* URLs/domains in the body
+* Attachment hashes
+* Suspicious subjects or message IDs
+
+## Success Criteria
+
+By the end of the lab, you should be able to:
+
+* Explain why the email is suspicious
+* List the key IOCs
+* Demonstrate safe handling of email artifacts
+
+## Optional Extensions
+
+* Import the `.eml` file into a sandboxed mail client and compare findings.
+* Run `whois` or `dig` on domains in the email (inside a VM).
+* Convert findings into SIEM detections or alert rules.
