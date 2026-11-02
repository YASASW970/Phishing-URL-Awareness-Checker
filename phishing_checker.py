import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check a URL for common warning signs."""

    raw_url = raw_url.strip()

    if not raw_url:
        raise ValueError("Please enter a URL.")

    parsed_url = urlparse(raw_url)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.hostname:
        raise ValueError(
            "Invalid URL. Enter a complete URL starting with http:// or https://"
        )

    warnings = []

    # Check 1: Look for an @ symbol.
    if "@" in raw_url:
        warnings.append("The URL contains an @ symbol.")

    # Check 2: Check whether the URL is unusually long.
    if len(raw_url) > 100:
        warnings.append("The URL is unusually long.")

    # Check 3: Check whether the hostname looks like an IPv4 address.
    hostname = parsed_url.hostname

    ipv4_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

    if re.match(ipv4_pattern, hostname):
        warnings.append("The hostname appears to be an IP address.")

    # Check 4: Check for many hostname parts.
    hostname_parts = hostname.split(".")

    if len(hostname_parts) >= 5:
        warnings.append("The hostname contains many parts.")

    # Check 5: Look for a punycode label.
    if "xn--" in hostname.lower():
        warnings.append("The hostname contains a punycode label.")

    # Check 6: Check whether the URL uses HTTP.
    if parsed_url.scheme.lower() == "http":
        warnings.append("The URL uses HTTP instead of HTTPS.")

    return warnings


def display_url_report(url):
    """Display a detailed report about the URL."""

    parsed_url = urlparse(url.strip())
    warnings = inspect_url(url)

    print("\n========== URL ANALYSIS REPORT ==========")
    print("URL:", url)
    print("Protocol:", parsed_url.scheme.upper())
    print("Hostname:", parsed_url.hostname)
    print("URL Length:", len(url.strip()), "characters")

    print("\nWarning Signs:")

    if warnings:
        for warning in warnings:
            print("-", warning)
    else:
        print("- No listed warning signs detected.")

    print("\nSecurity Reminder:")
    print("This report cannot confirm whether a website is safe.")
    print("Always verify a website before sharing sensitive information.")
    print("=========================================")


def main():
    print("=" * 45)
    print("EWB PHISHING URL AWARENESS CHECKER")
    print("This program checks URL text only.")
    print("It does not open or visit websites.")
    print("=" * 45)

    url = input("\nEnter a URL to check: ")

    try:
        display_url_report(url)

    except ValueError as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()