"""
13. ROMAN TO INTEGER - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Roman numerals are represented by seven symbols:

I  → 1
V  → 5
X  → 10
L  → 50
C  → 100
D  → 500
M  → 1000

Given a Roman numeral string s, convert it to an integer.

Rules:
- Roman numerals are usually written largest to smallest.
- However, there are special subtraction cases:
    - I before V or X  → 4, 9
    - X before L or C  → 40, 90
    - C before D or M  → 400, 900

------------------------------------------------
APPROACH 1: BRUTE FORCE (LEFT + RIGHT LOOKUP)
------------------------------------------------
INTUITION:
- For each character, compare it with the next character.
- If current value < next value, subtract it.
- Otherwise, add it.

WHY IT WORKS:
- Subtraction cases always appear as a smaller value
  before a larger value.
- This rule handles all Roman numeral patterns.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- This is the EXPECTED and OPTIMAL approach.
- No need for multiple passes.

------------------------------------------------
APPROACH 2: REVERSE TRAVERSAL (ALTERNATIVE VIEW)
------------------------------------------------
INTUITION:
- Traverse from right to left.
- Keep track of the previous value.
- If current value < previous value → subtract.
- Else → add.

WHY IT WORKS:
- Same logic as forward traversal.
- Sometimes easier to reason about.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- Optional explanation.
- Forward approach is usually clearer.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Single character (e.g., "V")
- All additive cases (e.g., "VIII")
- All subtractive cases (e.g., "IV", "IX")
- Maximum Roman numeral ("MMMCMXCIV")

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# OPTIMAL SOLUTION (LEFT TO RIGHT)
# ------------------------------------------------
def romanToInt(s):
    """
    Converts Roman numeral to integer.

    Parameters:
    s (str): Roman numeral string

    Returns:
    int: Integer value
    """

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    n = len(s)

    for i in range(n):
        value = roman[s[i]]

        # If next symbol exists and is larger, subtract
        if i + 1 < n and roman[s[i + 1]] > value:
            total -= value
        else:
            total += value

    return total


# ------------------------------------------------
# ALTERNATIVE SOLUTION (RIGHT TO LEFT)
# ------------------------------------------------
def romanToInt_reverse(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total = 0
    prev = 0

    for ch in reversed(s):
        value = roman[ch]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value

    return total


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    s = "MCMXCIV"

    print("Roman numeral:", s)

    print("\nOptimal Result (Left to Right):", romanToInt(s))

    print("Reverse Traversal Result:", romanToInt_reverse(s))
