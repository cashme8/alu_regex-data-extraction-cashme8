"""
Test Cases for Regex Data Extraction
"""

from main import extract_data, PATTERNS

# Define test samples for each category
TEST_INPUTS = {
    "emails": "Send to user@example.com and firstname.lastname@company.co.uk, not user@@wrong.",
    "urls": "Checkout https://www.example.com and http://test.org/page. Avoid ftp://files.com.",
    "phones": "Formats: (123) 456-7890, 123-456-7890, 123.456.7890, and wrong: 12-345-678.",
    "credit_cards": "Valid: 1234-5678-9012-3456, 1234 5678 9012 3456. Wrong: 12345678901234.",
    "times": "Meet at 14:30, 09:15, or 2:30 PM. Wrong: 25:00, 13:99."
}

def run_tests():
    print("=== Running Test Cases ===")
    for key, sample in TEST_INPUTS.items():
        print(f"\nTesting {key.capitalize()}:")
        matches = extract_data(sample, PATTERNS[key])
        print("Matches:", matches)

if __name__ == "__main__":
    run_tests()