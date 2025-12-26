"""
189. ROTATE ARRAY - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an integer array nums, rotate the array to the right
by k steps, where k is non-negative.

- Rotation is done IN-PLACE.
- k may be larger than the array length.

------------------------------------------------
APPROACH 1: BRUTE FORCE (ROTATE ONE BY ONE)
------------------------------------------------
INTUITION:
- Rotate the array to the right by 1 step, k times.
- Each single rotation shifts all elements by one position.

WHY IT WORKS:
- Directly simulates the rotation process.

TIME AND SPACE COMPLEXITY:
- Time: O(n * k)
- Space: O(1)

INTERVIEW NOTE:
- Too slow for large k.
- Not acceptable for optimal solutions.

------------------------------------------------
APPROACH 2: BETTER (USING EXTRA ARRAY)
------------------------------------------------
INTUITION:
- Use an extra array to place elements in their
  rotated positions.
- New index = (current_index + k) % n.

WHY IT WORKS:
- Modular arithmetic ensures correct rotation.

TIME AND SPACE COMPLEXITY:
- Time: O(n)
- Space: O(n)

INTERVIEW NOTE:
- Efficient but uses extra space.
- Acceptable only if space is allowed.

------------------------------------------------
APPROACH 3: OPTIMAL (REVERSAL ALGORITHM)
------------------------------------------------
INTUITION:
- Reverse the entire array.
- Reverse the first k elements.
- Reverse the remaining n-k elements.

WHY IT WORKS:
- Reversing rearranges elements to desired order.
- Achieves rotation without extra space.

TIME AND SPACE COMPLEXITY:
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- MOST IMPORTANT solution.
- Frequently asked in interviews.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def rotate_bruteforce(nums, k):
    n = len(nums)
    k %= n

    for _ in range(k):
        last = nums[-1]
        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]
        nums[0] = last


# ------------------------------------------------
# BETTER SOLUTION (EXTRA ARRAY)
# ------------------------------------------------
def rotate_better(nums, k):
    n = len(nums)
    k %= n

    temp = [0] * n

    for i in range(n):
        temp[(i + k) % n] = nums[i]

    for i in range(n):
        nums[i] = temp[i]


# ------------------------------------------------
# OPTIMAL SOLUTION (REVERSAL METHOD)
# ------------------------------------------------
def rotate(nums, k):
    n = len(nums)
    k %= n

    # Helper function to reverse part of the array
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Step 1: Reverse the whole array
    reverse(0, n - 1)

    # Step 2: Reverse first k elements
    reverse(0, k - 1)

    # Step 3: Reverse remaining elements
    reverse(k, n - 1)


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    print("Original array:", nums)

    # Brute force
    nums1 = nums.copy()
    rotate_bruteforce(nums1, k)
    print("\nBrute Force Result:", nums1)

    # Better
    nums2 = nums.copy()
    rotate_better(nums2, k)
    print("Better (Extra Array) Result:", nums2)

    # Optimal
    nums3 = nums.copy()
    rotate(nums3, k)
    print("Optimal (Reversal) Result:", nums3)
