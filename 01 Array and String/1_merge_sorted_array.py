"""
88. MERGE SORTED ARRAY - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order, and two integers m and n.

- nums1 has a length of m + n
- The first m elements of nums1 represent valid elements
- The last n elements of nums1 are set to 0 and should be ignored
- nums2 has n elements

Merge nums2 into nums1 so that nums1 becomes a single
sorted array.

IMPORTANT:
- The merge must be done IN-PLACE.
- Do NOT return anything, modify nums1 directly.

------------------------------------------------
APPROACH (INTUITION):
------------------------------------------------
- Since nums1 has extra space at the end, we can merge
  from the BACK instead of the front.
- Compare the largest remaining elements from nums1 and nums2.
- Place the larger element at the last available position.
- Decrease pointers accordingly.
- This avoids overwriting elements in nums1.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Both arrays are already sorted.
- Filling from the end ensures no useful data is lost.
- Each element is placed exactly once in correct position.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(m + n) → each element is processed once

Space Complexity:
- O(1) → in-place merge, no extra space used

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- This is a classic TWO POINTER problem.
- Many candidates mistakenly try merging from the front.
- Interviewers expect the backward merge approach.
- Returning nums1 is NOT required.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- nums2 is empty → nums1 remains unchanged
- nums1 has no valid elements (m = 0)
- Arrays with duplicate values
- All elements of nums2 are smaller or larger than nums1

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def merge(nums1, m, nums2, n):
    """
    Merges nums2 into nums1 as one sorted array (in-place).

    Parameters:
    nums1 (list): First sorted array with extra space
    m (int): Number of valid elements in nums1
    nums2 (list): Second sorted array
    n (int): Number of elements in nums2

    Returns:
    None (nums1 is modified in-place)
    """

    # Pointer for last valid element in nums1
    i = m - 1

    # Pointer for last element in nums2
    j = n - 1

    # Pointer for last position in nums1
    k = m + n - 1

    # Merge from the back
    while i >= 0 and j >= 0:

        # Place the larger element at the end
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    # Copy remaining elements of nums2 (if any)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    print("Before merge:")
    print("nums1:", nums1)
    print("nums2:", nums2)

    # Merge arrays
    merge(nums1, m, nums2, n)

    print("\nAfter merge:")
    print("nums1:", nums1)
