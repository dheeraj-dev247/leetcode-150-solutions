"""
42. TRAPPING RAIN WATER - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it
can trap after raining.

------------------------------------------------
APPROACH 1: BRUTE FORCE
------------------------------------------------
INTUITION:
- For each index i:
  - Find the maximum height to its left.
  - Find the maximum height to its right.
- Water trapped at i =
    min(max_left, max_right) - height[i]

WHY IT WORKS:
- Water level is limited by the shorter boundary.
- Directly follows the physical definition.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n²)
- Space: O(1)

INTERVIEW NOTE:
- Easy to derive.
- Too slow for large inputs.

------------------------------------------------
APPROACH 2: BETTER (PREFIX & SUFFIX MAX ARRAYS)
------------------------------------------------
INTUITION:
- Precompute:
  - left_max[i] = max height from 0 to i
  - right_max[i] = max height from i to n-1
- For each index:
  water[i] = min(left_max[i], right_max[i]) - height[i]

WHY IT WORKS:
- Avoids repeated scanning.
- Same logic as brute force but optimized.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(n)

INTERVIEW NOTE:
- Very common intermediate solution.
- Sets up intuition for optimal approach.

------------------------------------------------
APPROACH 3: OPTIMAL (TWO POINTERS)
------------------------------------------------
INTUITION:
- Use two pointers: left and right.
- Maintain left_max and right_max.
- Move the pointer with the smaller height.
- Water trapped depends on the smaller side.

WHY IT WORKS:
- Water level is decided by the minimum boundary.
- Greedy pointer movement guarantees correctness.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- EXPECTED solution in interviews.
- Classic two-pointer problem.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array
- Less than 3 bars → no water
- Flat elevation map

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def trap_bruteforce(height):
    n = len(height)
    water = 0

    for i in range(n):
        left_max = max(height[: i + 1])
        right_max = max(height[i:])

        water += min(left_max, right_max) - height[i]

    return water


# ------------------------------------------------
# BETTER SOLUTION (PREFIX & SUFFIX ARRAYS)
# ------------------------------------------------
def trap_better(height):
    n = len(height)
    if n == 0:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


# ------------------------------------------------
# OPTIMAL SOLUTION (TWO POINTERS)
# ------------------------------------------------
def trap(height):
    """
    Calculates trapped rain water using two pointers.

    Parameters:
    height (list): Elevation map

    Returns:
    int: Total trapped water
    """

    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:

        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    print("Elevation map:", height)

    print("\nBrute Force Result:", trap_bruteforce(height))

    print("Better (Prefix & Suffix) Result:", trap_better(height))

    print("Optimal (Two Pointers) Result:", trap(height))
