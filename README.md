# Phishing Email Analysis Lab

This repository contains a click by click lab guide for safely analyzing phishing emails and documenting indicators of compromise.

The lab covers:

- Setting up a safe virtual environment (e.g., Kali Linux or Ubuntu VM) and installing analysis tools such as Thunderbird, exiftool, whois, 7 Zip, ClamAV and oletools.
- Importing a phishing email (.eml file) into a mail client without interacting with any links or attachments.
- Inspecting email headers to verify sender addresses, Received chains and authentication results.
- Examining the email body to identify social engineering techniques and mismatched URLs.
- Extracting and scanning attachments, watching for suspicious file names or extensions, and analyzing metadata and macros.
- Documenting findings, indicators of compromise, and remediation steps.

See the Word document [`phishing_email_analysis_lab_guide.docx`](phishing_email_analysis_lab_guide.docx) for detailed instructions, screenshots and guidance.

## Project Structure

```
phishing-email-analysis-lab/
├ phishing_email_analysis_lab_guide.docx – Comprehensive lab guide.
└ README.md – Overview of the project.
```

## Getting Started

1. Provision a virtual machine (e.g., Kali Linux).
2. Install the required tools listed in the lab guide.
3. Import a sample phishing email into your mail client.
4. Follow the guide to analyze headers, body and attachments, and record your observations.
5. Use the findings to improve awareness and detection of phishing attempts.
