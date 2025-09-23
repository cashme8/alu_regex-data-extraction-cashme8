"""
Regex Data Extraction Tool
Author: Gislain
Description:

Extracts emails, URLs, phone numbers, credit cards, and time formats
from a given text input using Regular Expressions.

Breakdown: Purpose → Demo of how the regex works.
Contains a sample text with emails, URLs, phones, cards, and times.
Runs once and prints all matches it finds.
It’s like a showcase of the tool.
"""

import re

# ==============================
# Regex Patterns
# ==============================

REGEX_PATTERNS = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "urls": r"https?://[^\s]+",
    "phones": r"(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})",
    "credit_cards": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
    "times": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b",
}

# ==============================
# Functions
# ==============================

def extract_the_data(text: str, pattern: str):
    """Extracts all matches of the given regex pattern from the input text."""
    return re.findall(pattern, text)


def run_me():
    """Runs demo extractions on a sample text."""
    sample_text = """
    Contact me at kabandagislain440@#gmail.com or king@company.co.uk.
    Visit https://irembo.gov.rw/ or https://etax.rra.gov.rw/.
    Call me at (250) 786-7890, 123-456-7890 or 123.456.7890.
    My credit card: 1234-5678-9012-3456 or 1234 5678 9012 3456.
    Meeting at 14:30 or 2:30 PM.
    """

    print("=== Regex Data Extraction run_me Demo ===")
    for key, pattern in REGEX_PATTERNS.items():
        print(f"\n{key.capitalize()}:")
        results = extract_the_data(sample_text, pattern)
        print(results if results else "No matches found.")


if __name__ == "__main__":
    run_me()
