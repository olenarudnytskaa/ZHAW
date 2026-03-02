"""
Context:
Hospitals exchange patient data as text. To ensure consistent formatting, it helps to
understand ASCII codes for names or other text-based data (e.g., ICD codes).

Exercise:
Resolve all the TODOs.

Test with a sample patient name (e.g., "Alice") to ensure the round-trip conversion works.
"""


def string_to_ascii_codes(text: str) -> list:
    # TODO: return an array of ASCII codes, e.g., [65, 108, 105, 99, 101] for "Alice"
    return [ord(char) for char in text]
    pass


def ascii_codes_to_string(codes: list) -> str:
    # TODO: return a string representing the given codes, e.g., "Alice" for [65, 108, 105, 99, 101]
    return "".join(chr(code) for code in codes)
    pass


if __name__ == "__main__":
    patient_name = "Alice"
    ascii_list = string_to_ascii_codes(patient_name)
    print("ASCII/UTF Codes:", ascii_list)

    recovered_name = ascii_codes_to_string(ascii_list)
    print("Recovered Name:", recovered_name)
