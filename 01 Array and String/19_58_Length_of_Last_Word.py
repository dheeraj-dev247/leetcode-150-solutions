"""
58. LENGTH OF LAST WORD - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given a string s consisting of words and spaces,
return the length of the LAST word in the string.

- A word is a maximal substring consisting of
  non-space characters only.
- The string may contain leading/trailing spaces.
- It is guaranteed that there is at least one word.

------------------------------------------------
APPROACH 1: BRUTE FORCE (SPLIT)
------------------------------------------------
INTUITION:
- Split the string by spaces.
- The last element after split is the last word.
- Return its length.

WHY IT WORKS:
- split() automatically removes extra spaces.
- Directly extracts words.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(n)  (extra list created)

INTERVIEW NOTE:
- PERFECTLY ACCEPTABLE in most interviews.
- Clean and readable.
- Often the first solution interviewers expect.

------------------------------------------------
APPROACH 2: BETTER (REVERSE SCAN WITH EXTRA VARIABLES)
------------------------------------------------
INTUITION:
- Scan the string from the end.
- Skip trailing spaces.
- Count characters until a space is found.

WHY IT WORKS:
- Directly finds the last word.
- Avoids creating a list of words.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- Expected if interviewer asks for space optimization.

------------------------------------------------
APPROACH 3: OPTIMAL (SAME AS APPROACH 2)
------------------------------------------------
NOTE:
- Approach 2 is already optimal.
- There is no faster-than-O(n) solution since
  the string must be inspected.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- "Hello World" → 5
- "   fly me   to   the moon  " → 4
- "a" → 1
- "   a   " → 1

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION (USING SPLIT)
# ------------------------------------------------
def lengthOfLastWord_split(s):
    """
    Returns length of last word using split.

    Parameters:
    s (str): Input string

    Returns:
    int: Length of last word
    """

    words = s.split()
    return len(words[-1])


# ------------------------------------------------
# OPTIMAL SOLUTION (O(1) EXTRA SPACE)
# ------------------------------------------------
def lengthOfLastWord(s):
    """
    Returns length of last word using reverse scan.

    Parameters:
    s (str): Input string

    Returns:
    int: Length of last word
    """

    length = 0
    i = len(s) - 1

    # Skip trailing spaces
    while i >= 0 and s[i] == " ":
        i -= 1

    # Count characters of last word
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1

    return length


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    s = "   fly me   to   the moon  "

    print("Input string:", repr(s))

    print("\nBrute Force Result:", lengthOfLastWord_split(s))

    print("Optimal Result:", lengthOfLastWord(s))
