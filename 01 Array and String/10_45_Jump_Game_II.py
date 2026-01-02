"""
45. JUMP GAME II - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given an integer array nums where nums[i] represents
the maximum jump length from index i.

- You start at index 0.
- Return the MINIMUM number of jumps needed to reach
  the last index.
- You can assume you can always reach the last index.

------------------------------------------------
APPROACH 1: BRUTE FORCE (RECURSION)
------------------------------------------------
INTUITION:
- From each index, try all possible jumps.
- Take the minimum jumps among all choices.

WHY IT WORKS:
- Explores every possible path to the end.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: Exponential
- Space: O(n) recursion stack

INTERVIEW NOTE:
- Conceptual only.
- Not acceptable for large inputs.

------------------------------------------------
APPROACH 2: BETTER (DYNAMIC PROGRAMMING)
------------------------------------------------
INTUITION:
- dp[i] = minimum jumps needed to reach index i.
- For each index, update reachable positions.

WHY IT WORKS:
- Stores optimal subproblem results.
- Avoids recomputation.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n²)
- Space: O(n)

INTERVIEW NOTE:
- Correct but not optimal.
- May TLE for large arrays.

------------------------------------------------
APPROACH 3: OPTIMAL (GREEDY – LEVEL / RANGE BASED)
------------------------------------------------
INTUITION:
- Think in terms of "levels" like BFS.
- Each jump defines a reachable RANGE.
- When you finish scanning the current range,
  you must take a jump and move to the next range.

KEY VARIABLES:
- farthest: farthest index reachable so far
- current_end: end of current jump range
- jumps: number of jumps taken

WHY IT WORKS:
- At each level, we greedily extend the reach as far as possible.
- When current range ends, we commit one jump.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- MOST IMPORTANT solution.
- Same greedy idea as Jump Game I, with jump counting.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION (RECURSION)
# ------------------------------------------------
def jump_bruteforce(nums):

    def dfs(index):
        if index >= len(nums) - 1:
            return 0

        min_jumps = float("inf")
        for step in range(1, nums[index] + 1):
            min_jumps = min(min_jumps, 1 + dfs(index + step))

        return min_jumps

    return dfs(0)


# ------------------------------------------------
# BETTER SOLUTION (DP)
# ------------------------------------------------
def jump_dp(nums):
    n = len(nums)
    dp = [float("inf")] * n
    dp[0] = 0

    for i in range(n):
        for step in range(1, nums[i] + 1):
            if i + step < n:
                dp[i + step] = min(dp[i + step], dp[i] + 1)

    return dp[-1]


# ------------------------------------------------
# OPTIMAL SOLUTION (GREEDY)
# ------------------------------------------------
def jump(nums):
    """
    Returns the minimum number of jumps to reach last index.

    Parameters:
    nums (list): Jump lengths

    Returns:
    int: Minimum number of jumps
    """

    jumps = 0
    current_end = 0
    farthest = 0

    # We stop at len(nums) - 2 because
    # once we reach the last index, no more jumps needed
    for i in range(len(nums) - 1):

        # Update the farthest reachable index
        farthest = max(farthest, i + nums[i])

        # If we reached the end of current jump range
        if i == current_end:
            jumps += 1
            current_end = farthest

    return jumps


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    nums = [2, 3, 1, 1, 4]

    print("Array:", nums)

    print("\nBrute Force Result:", jump_bruteforce(nums))

    print("DP Result:", jump_dp(nums))

    print("Optimal (Greedy) Result:", jump(nums))
