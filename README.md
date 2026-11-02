# Phishing URL Awareness Checker

## 1. Project Overview

The Phishing URL Awareness Checker is a beginner-friendly cybersecurity project developed using Python.

It checks the text of a URL for common warning signs that may be associated with phishing attacks. The program does not open or visit websites.

## 2. Features

* Detects the @ symbol in a URL.
* Checks whether a URL is unusually long.
* Identifies hostnames that appear to be IPv4 addresses.
* Checks for hostnames with many parts.
* Detects punycode-style hostnames.
* Identifies URLs that use HTTP instead of HTTPS.
* Displays a detailed URL analysis report.
* Shows the protocol, hostname, URL length, and detected warning signs.
* Displays a security reminder.

## 3. Requirements

* Python 3.10 or later.
* Visual Studio Code or another Python editor.
* No additional Python packages are required.

## 4. How to Run

1. Open the project folder in VS Code.

2. Open the terminal.

3. Run the following command:

   `python phishing_checker.py`

4. Enter a sample URL when prompted.

5. Review the URL analysis report displayed in the terminal.

## 5. Testing

The program is tested using five sample URLs from the project guide.

The test cases and their actual results are documented in `tests/test_samples.md`.

## 6. Screenshots

### Sample Program Run

![Sample Run](screenshots/sample_run.png)

### Test Results

![Test Results](screenshots/test_results.png)

## 7. Improvements

1. **Detailed URL Analysis Report:** Displays the entered URL, protocol, hostname, URL length, and detected warning signs.
2. **Security Reminder:** Reminds users that the program cannot guarantee that a website is safe.

## 8. Limitations

This is an educational cybersecurity awareness tool. It checks URL text only. It does not visit websites, scan for malware, or verify a website's reputation.

A URL with no detected warning signs may still be malicious.

## 9. Ethical Use

Use the sample URLs provided in the project guide. Do not enter passwords or other sensitive information into suspicious websites.

## 10. Author

Yasaswi Ramisetty

Cybersecurity Internship — EWB Courses
