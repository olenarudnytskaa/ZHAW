"""
Context:
Imagine you have a medical device outputting patient record identifiers as decimal numbers.
For diagnostics or debugging, you may need to convert those identifiers into binary or
hexadecimal forms, and vice versa.

Exercise:
Resolve all the TODOs.

Then test these functions by converting a decimal ID (e.g., 2025) to binary, then to hex,
and finally convert the binary string back to decimal.
"""


def decimal_to_binary(num: int) -> str:
    if num == 0:
        return "0"
    binary_digits = []
    while num > 0:
        remainder = num % 2  # TODO: Calculate the remainder when dividing 'num' by 2 (tip: modulo operator)
        binary_digits.append(str(remainder))
        num = num // 2 # ... # TODO: divide 'num' by 2 and keep only the whole number part (tip: floor division operator)
    binary_digits.reverse()
    return "".join(binary_digits)


def decimal_to_hex(num: int) -> str:
    if num == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hex_digits = []
    while num > 0:
        remainder = num % 16  # TODO: Calculate the remainder like above but for hex
        hex_digits.append(hex_chars[remainder])
        num = num // 16 # ... # TODO: Calculate 'num' as above but for hex
    hex_digits.reverse()
    return "".join(hex_digits)


def binary_to_decimal(bin_str: str) -> int:
    """
    Converts a binary string to its decimal representation.

    TODO: Implement one of the two solutions below.

    Option 1: Iterative approach
    - Initialize `decimal_value` to 0.
    - Iterate through each digit in `bin_str`.
    - Update `decimal_value` by multiplying by 2 and adding the integer value of the digit.

    Option 2: Positional value approach
    - Reverse the string and enumerate through it.
    - Multiply each digit by 2 raised to the power of its position.
    - Sum up the results to get the decimal value.
    """

    decimal_value = 0


    # TODO: Implement Option 1 (Iterative approach) or Option 2 (Positional value approach)
    for digit in bin_str:
        decimal_value = decimal_value * 2 + int(digit)

    return decimal_value


if __name__ == "__main__":
    patient_id_decimal = 2025
    print("Decimal:", patient_id_decimal)

    binary_rep = decimal_to_binary(patient_id_decimal)
    print("Binary:", binary_rep)
    print("Built-in Binary:", bin(patient_id_decimal))

    hex_rep = decimal_to_hex(patient_id_decimal)
    print("Hex:", hex_rep)
    print("Built-in Hex:", hex(patient_id_decimal))

    recovered_decimal = binary_to_decimal(binary_rep)
    print("Recovered Decimal from Binary:", recovered_decimal)
