"""
14. LONGEST COMMON PREFIX - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Write a function to find the longest common prefix string
amongst an array of strings.

- If there is no common prefix, return an empty string "".
- All input strings consist of lowercase letters.

------------------------------------------------
APPROACH 1: BRUTE FORCE (HORIZONTAL SCANNING)
------------------------------------------------
INTUITION:
- Assume the first string is the prefix.
- Compare it with each subsequent string.
- Shorten the prefix until it matches.

WHY IT WORKS:
- Gradually reduces the prefix until it fits all strings.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n * m)
  where n = number of strings, m = length of prefix
- Space: O(1)

INTERVIEW NOTE:
- Very common and acceptable solution.
- Easy to explain and implement.

------------------------------------------------
APPROACH 2: BETTER (VERTICAL SCANNING)
------------------------------------------------
INTUITION:
- Compare characters column by column.
- Stop when a mismatch is found.

WHY IT WORKS:
- Efficiently detects the first mismatch.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n * m)
- Space: O(1)

INTERVIEW NOTE:
- Clean and intuitive.
- Slightly more elegant than horizontal scanning.

------------------------------------------------
APPROACH 3: OPTIMAL (SORTING)
------------------------------------------------
INTUITION:
- Sort the array of strings.
- Only compare the first and last strings.
- Their common prefix is the answer.

WHY IT WORKS:
- Sorting brings similar strings closer.
- First and last differ the most.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n log n)
- Space: O(1) or O(n) depending on sort

INTERVIEW NOTE:
- Clever trick.
- Not always faster due to sorting cost.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array
- Single string
- No common prefix
- All strings same

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# APPROACH 1: HORIZONTAL SCANNING
# ------------------------------------------------
def longestCommonPrefix_horizontal(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""

    return prefix


# ------------------------------------------------
# APPROACH 2: VERTICAL SCANNING
# ------------------------------------------------
def longestCommonPrefix_vertical(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i == len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]


# ------------------------------------------------
# APPROACH 3: SORTING
# ------------------------------------------------
def longestCommonPrefix_sorting(strs):
    if not strs:
        return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]
    i = 0

    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    strs = ["flower", "flow", "flight"]

    print("Strings:", strs)

    print("\nHorizontal Scanning Result:", longestCommonPrefix_horizontal(strs))

    print("Vertical Scanning Result:", longestCommonPrefix_vertical(strs))

    print("Sorting-Based Result:", longestCommonPrefix_sorting(strs))
