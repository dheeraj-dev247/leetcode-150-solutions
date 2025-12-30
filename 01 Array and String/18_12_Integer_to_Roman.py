"""
12. INTEGER TO ROMAN - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an integer num, convert it to a Roman numeral.

Roman numeral rules:
- Symbols and values:
    I  → 1
    V  → 5
    X  → 10
    L  → 50
    C  → 100
    D  → 500
    M  → 1000

- Subtractive cases:
    IV  → 4
    IX  → 9
    XL  → 40
    XC  → 90
    CD  → 400
    CM  → 900

Constraints:
- 1 <= num <= 3999

------------------------------------------------
APPROACH: GREEDY (OPTIMAL)
------------------------------------------------
INTUITION:
- Always take the largest Roman value less than or equal to num.
- Append its symbol to the result.
- Subtract its value from num.
- Repeat until num becomes 0.

WHY THIS APPROACH WORKS:
- Roman numerals are constructed greedily from largest to smallest.
- Subtractive cases are just special values and fit naturally
  into the greedy process.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(1) → The number of Roman symbols is fixed and small.

Space Complexity:
- O(1) → Output size is bounded (max length ~15).

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- No brute force is needed; greedy is the expected solution.
- Always include subtractive pairs in the mapping.
- Order of values is CRITICAL (largest → smallest).

------------------------------------------------
EDGE CASES:
------------------------------------------------
- num = 1 → "I"
- num = 4 → "IV"
- num = 9 → "IX"
- num = 3999 → "MMMCMXCIX"

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def intToRoman(num):
    """
    Converts an integer to a Roman numeral.

    Parameters:
    num (int): Integer between 1 and 3999

    Returns:
    str: Roman numeral representation
    """

    # Ordered list of (value, symbol)
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = []

    for value, symbol in values:
        while num >= value:
            result.append(symbol)
            num -= value

    return "".join(result)


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    num = 1994

    print("Integer:", num)
    print("Roman Numeral:", intToRoman(num))
