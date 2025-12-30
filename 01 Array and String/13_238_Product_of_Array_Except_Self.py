"""
238. PRODUCT OF ARRAY EXCEPT SELF - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an integer array nums, return an array answer such that:

answer[i] = product of all elements of nums except nums[i]

Constraints:
- You must solve it WITHOUT using division.
- Time complexity must be O(n).
- Space complexity should be O(1) (excluding output array).

------------------------------------------------
APPROACH 1: BRUTE FORCE
------------------------------------------------
INTUITION:
- For each index i, compute the product of all elements
  except nums[i] by looping through the array.

WHY IT WORKS:
- Directly follows the problem definition.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n²)
- Space: O(1) (excluding output)

INTERVIEW NOTE:
- Easy to understand.
- Too slow for large inputs.

------------------------------------------------
APPROACH 2: BETTER (PREFIX & SUFFIX ARRAYS)
------------------------------------------------
INTUITION:
- Precompute prefix products:
  prefix[i] = product of elements before i
- Precompute suffix products:
  suffix[i] = product of elements after i
- answer[i] = prefix[i] * suffix[i]

WHY IT WORKS:
- Avoids repeated multiplication.
- Clean separation of left and right products.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(n)

INTERVIEW NOTE:
- Very common intermediate solution.
- Sets up intuition for the optimal approach.

------------------------------------------------
APPROACH 3: OPTIMAL (IN-PLACE PREFIX PRODUCT)
------------------------------------------------
INTUITION:
- Store prefix product directly in output array.
- Then traverse from right while maintaining a suffix product.
- Multiply prefix and suffix on the fly.

WHY IT WORKS:
- Reuses output array to save space.
- Maintains O(n) time and O(1) extra space.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1) extra space (output excluded)

INTERVIEW NOTE:
- EXPECTED solution.
- Very important array manipulation problem.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def productExceptSelf_bruteforce(nums):
    n = len(nums)
    result = [1] * n

    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        result[i] = prod

    return result


# ------------------------------------------------
# BETTER SOLUTION (PREFIX + SUFFIX ARRAYS)
# ------------------------------------------------
def productExceptSelf_better(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    result = [1] * n

    # Build prefix products
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Build suffix products
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Build result
    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result


# ------------------------------------------------
# OPTIMAL SOLUTION (O(1) EXTRA SPACE)
# ------------------------------------------------
def productExceptSelf(nums):
    """
    Returns the product of array except self.

    Parameters:
    nums (list): List of integers

    Returns:
    list: Product array
    """

    n = len(nums)
    result = [1] * n

    # Step 1: Prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Step 2: Suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    nums = [1, 2, 3, 4]

    print("Input:", nums)

    print("\nBrute Force Result:", productExceptSelf_bruteforce(nums))

    print("Better (Prefix + Suffix) Result:", productExceptSelf_better(nums))

    print("Optimal Result:", productExceptSelf(nums))
