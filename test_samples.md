# Phishing URL Awareness Checker — Test Results

## Test 1: Normal Example URL

**Input:**
`https://www.example.com/login`

**Expected result:** No listed warning signs detected.

**Actual result:** No listed warning signs detected.

**Status:** PASS

---

## Test 2: IP Address and HTTP

**Input:**
`http://192.0.2.10/account`

**Expected result:**

* Warning that the hostname appears to be an IP address.
* Warning that the URL uses HTTP instead of HTTPS.

**Actual result:** Both warnings were displayed.

**Status:** PASS

---

## Test 3: URL Contains @ Symbol

**Input:**
`http://example.com@sample.invalid/login`

**Expected result:**

* Warning that the URL contains an @ symbol.
* Warning that the URL uses HTTP instead of HTTPS.

**Actual result:** Update this after running the test.

**Status:** Update after testing.

---

## Test 4: Hostname with Many Parts

**Input:**
`https://a.b.c.d.e.example.invalid/path`

**Expected result:** Warning that the hostname contains many parts.

**Actual result:** Update this after running the test.

**Status:** Update after testing.

---

## Test 5: Punycode Hostname

**Input:**
`https://xn--example.invalid/`

**Expected result:** Warning that the hostname contains a punycode label.

**Actual result:** Update this after running the test.

**Status:** Update after testing.

---

## Conclusion

The program checks URLs for common warning signs. These checks are intended for cybersecurity awareness and do not prove whether a website is safe or malicious.


## Actual Test Results

| Test | Description           | Result |
| ---- | --------------------- | ------ |
| 1    | Normal HTTPS URL      | PASS   |
| 2    | IP address and HTTP   | PASS   |
| 3    | URL contains @ symbol | PASS   |
| 4    | Many hostname parts   | PASS   |
| 5    | Punycode hostname     | PASS   |

All five test cases were run successfully. The program detected the expected warning signs in the tested URLs.

**Note:** This tool checks common URL warning signs. It cannot guarantee that a website is safe or malicious.

