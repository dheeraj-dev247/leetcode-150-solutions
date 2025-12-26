"""
55. JUMP GAME - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given an integer array nums where nums[i] represents
the maximum jump length from index i.

- You start at index 0.
- Determine if you can reach the last index.
- Return True if reachable, otherwise False.

------------------------------------------------
APPROACH 1: BRUTE FORCE (RECURSION / BACKTRACKING)
------------------------------------------------
INTUITION:
- From each index, try all possible jumps.
- If any path reaches the last index, return True.

WHY IT WORKS:
- Explores all possible jump combinations.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: Exponential (worst-case)
- Space: O(n) recursion stack

INTERVIEW NOTE:
- Not efficient.
- Used only for conceptual understanding.

------------------------------------------------
APPROACH 2: BETTER (DYNAMIC PROGRAMMING)
------------------------------------------------
INTUITION:
- Use a DP array to mark reachable indices.
- dp[i] = True if index i can be reached.
- From each reachable index, mark further reachable positions.

WHY IT WORKS:
- Avoids recomputation.
- Ensures all reachable paths are tracked.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n²)
- Space: O(n)

INTERVIEW NOTE:
- Acceptable but not optimal.

------------------------------------------------
APPROACH 3: OPTIMAL (GREEDY)
------------------------------------------------
INTUITION:
- Track the farthest index reachable so far.
- If current index is beyond this, return False.
- Update farthest reach as you iterate.

WHY IT WORKS:
- Only the maximum reachable distance matters.
- Greedy choice always keeps best possible future.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- MOST EXPECTED solution.
- Very common greedy problem.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def canJump_bruteforce(nums):

    def dfs(index):
        if index >= len(nums) - 1:
            return True

        max_jump = nums[index]
        for jump in range(1, max_jump + 1):
            if dfs(index + jump):
                return True

        return False

    return dfs(0)


# ------------------------------------------------
# BETTER SOLUTION (DP)
# ------------------------------------------------
def canJump_dp(nums):
    n = len(nums)
    dp = [False] * n
    dp[0] = True

    for i in range(n):
        if dp[i]:
            for jump in range(1, nums[i] + 1):
                if i + jump < n:
                    dp[i + jump] = True

    return dp[n - 1]


# ------------------------------------------------
# OPTIMAL SOLUTION (GREEDY)
# ------------------------------------------------
def canJump(nums):
    """
    Determines if the last index is reachable.

    Parameters:
    nums (list): Jump lengths

    Returns:
    bool: True if reachable, False otherwise
    """

    farthest = 0

    for i in range(len(nums)):

        # If current index is not reachable
        if i > farthest:
            return False

        # Update farthest reachable index
        farthest = max(farthest, i + nums[i])

    return True


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    nums1 = [2, 3, 1, 1, 4]
    nums2 = [3, 2, 1, 0, 4]

    print("Array:", nums1)
    print("Can jump?", canJump(nums1))

    print("\nArray:", nums2)
    print("Can jump?", canJump(nums2))
