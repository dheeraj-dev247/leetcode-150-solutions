"""
88. MERGE SORTED ARRAY - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2.

Merge nums2 into nums1 as one sorted array.

IMPORTANT:
- nums1 has a length of m + n
- First m elements of nums1 are valid
- Last n elements are placeholders (0)
- nums2 has n elements

You must modify nums1 IN-PLACE.

------------------------------------------------
APPROACH 1: BRUTE FORCE (EXTRA SPACE)
------------------------------------------------
INTUITION:
- Combine both arrays.
- Sort the combined array.
- Copy back to nums1.

WHY IT WORKS:
- Sorting guarantees correct order.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O((m + n) log(m + n))
- Space: O(m + n)

INTERVIEW NOTE:
- Easy but NOT optimal.
- Fails in-place constraint.

------------------------------------------------
APPROACH 2: TWO POINTERS (USING EXTRA ARRAY)
------------------------------------------------
INTUITION:
- Use two pointers to merge like merge sort.
- Store result in temp array.

WHY IT WORKS:
- Both arrays are sorted.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(m + n)
- Space: O(m + n)

INTERVIEW NOTE:
- Logical but not in-place.

------------------------------------------------
APPROACH 3: OPTIMAL (TWO POINTERS FROM END - IN-PLACE)
------------------------------------------------
INTUITION:
- Merge from the END to avoid overwriting.
- Place largest elements first.

WHY IT WORKS:
- nums1 has extra space at the end.
- Backward traversal preserves data.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(m + n)
- Space: O(1)

INTERVIEW NOTE:
- EXPECTED SOLUTION.
- Frequently asked.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def merge_bruteforce(nums1, m, nums2, n):
    # Combine valid part of nums1 and all of nums2
    temp = nums1[:m] + nums2

    # Sort the combined array
    temp.sort()

    # Copy sorted values back to nums1
    for i in range(m + n):
        nums1[i] = temp[i]


# ------------------------------------------------
# BETTER SOLUTION (USING EXTRA ARRAY)
# ------------------------------------------------
def merge_better(nums1, m, nums2, n):
    temp = []  # Temporary array to store merged result
    i = j = 0  # Pointers for nums1 and nums2

    # Compare elements from nums1 and nums2
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            temp.append(nums1[i])  # Add smaller element
            i += 1
        else:
            temp.append(nums2[j])
            j += 1

    # Copy remaining elements from nums1 (if any)
    while i < m:
        temp.append(nums1[i])
        i += 1

    # Copy remaining elements from nums2 (if any)
    while j < n:
        temp.append(nums2[j])
        j += 1

    # Copy merged result back into nums1
    for i in range(m + n):
        nums1[i] = temp[i]


# ------------------------------------------------
# OPTIMAL SOLUTION (IN-PLACE FROM END)
# ------------------------------------------------
def merge(nums1, m, nums2, n):
    """
    Merges nums2 into nums1 in-place.
    """

    # Pointer to last valid element in nums1
    i = m - 1

    # Pointer to last element in nums2
    j = n - 1

    # Pointer to last index of nums1
    k = m + n - 1

    # Merge while both arrays have elements
    while i >= 0 and j >= 0:
        # Place the larger element at the end
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If nums2 still has elements, copy them
    # (No need to copy nums1 leftovers; they are already in place)
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3

    merge(nums1, m, nums2, n)
    print("Merged Array:", nums1)
