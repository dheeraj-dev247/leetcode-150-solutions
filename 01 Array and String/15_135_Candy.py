"""
135. CANDY - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
There are n children standing in a line.
Each child is assigned a rating value.

You are giving candies to these children subject to:
1. Each child must have at least one candy.
2. Children with a higher rating than their neighbors
   must get more candies than those neighbors.

Return the minimum number of candies you need to distribute.

------------------------------------------------
APPROACH 1: BRUTE FORCE (ADJUST UNTIL STABLE)
------------------------------------------------
INTUITION:
- Start by giving every child 1 candy.
- Repeatedly scan the array:
  - If a child has a higher rating than a neighbor
    but not more candies, increase candies.
- Continue until no violations remain.

WHY IT WORKS:
- Eventually satisfies all constraints.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n²) (may need many passes)
- Space: O(n)

INTERVIEW NOTE:
- Conceptual only.
- Inefficient and not recommended.

------------------------------------------------
APPROACH 2: BETTER (TWO ARRAYS: LEFT & RIGHT)
------------------------------------------------
INTUITION:
- Left pass:
  - If rating[i] > rating[i-1], candies[i] = candies[i-1] + 1
- Right pass:
  - If rating[i] > rating[i+1], candies[i] = max(candies[i], candies[i+1] + 1)
- Take max from both sides to satisfy both neighbors.

WHY IT WORKS:
- Left pass satisfies left neighbor rule.
- Right pass satisfies right neighbor rule.
- Max ensures both constraints hold.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(n)

INTERVIEW NOTE:
- Very clean and easy to explain.
- Accepted solution.

------------------------------------------------
APPROACH 3: OPTIMAL (GREEDY – SINGLE ARRAY)
------------------------------------------------
INTUITION:
- Give each child 1 candy initially.
- First left-to-right pass handles increasing ratings.
- Second right-to-left pass fixes decreasing ratings.
- Use only one array.

WHY IT WORKS:
- Same logic as two-array approach but space optimized.
- Ensures minimal candies.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(n)  (this is optimal for this problem)

INTERVIEW NOTE:
- THIS IS THE EXPECTED SOLUTION.
- O(1) space solution exists but is complex and rarely expected.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Single child
- All ratings equal
- Strictly increasing ratings
- Strictly decreasing ratings

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def candy_bruteforce(ratings):
    n = len(ratings)
    candies = [1] * n
    changed = True

    while changed:
        changed = False
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i - 1] + 1
                changed = True
            if (
                i < n - 1
                and ratings[i] > ratings[i + 1]
                and candies[i] <= candies[i + 1]
            ):
                candies[i] = candies[i + 1] + 1
                changed = True

    return sum(candies)


# ------------------------------------------------
# BETTER SOLUTION (TWO ARRAYS)
# ------------------------------------------------
def candy_better(ratings):
    n = len(ratings)
    left = [1] * n
    right = [1] * n

    # Left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1

    # Right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right[i] = right[i + 1] + 1

    total = 0
    for i in range(n):
        total += max(left[i], right[i])

    return total


# ------------------------------------------------
# OPTIMAL SOLUTION (ONE ARRAY, TWO PASSES)
# ------------------------------------------------
def candy(ratings):
    """
    Returns the minimum number of candies required.

    Parameters:
    ratings (list): Ratings of children

    Returns:
    int: Minimum candies
    """

    n = len(ratings)
    candies = [1] * n

    # Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right to left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    ratings = [1, 0, 2]

    print("Ratings:", ratings)

    print("\nBrute Force Result:", candy_bruteforce(ratings))

    print("Better (Two Arrays) Result:", candy_better(ratings))

    print("Optimal Result:", candy(ratings))
