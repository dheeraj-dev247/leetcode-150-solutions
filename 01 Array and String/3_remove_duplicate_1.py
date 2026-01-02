"""
26. REMOVE DUPLICATES FROM SORTED ARRAY - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given a sorted integer array nums, remove the duplicates
IN-PLACE such that each unique element appears only once.

- The relative order of the elements should be preserved.
- Return the number of unique elements (k).
- It does NOT matter what values are left beyond the
  returned length.

------------------------------------------------
APPROACH (INTUITION):
------------------------------------------------
- Since the array is already sorted, duplicates will
  appear next to each other.
- Use a TWO POINTER technique.
- One pointer (write index) keeps track of the position
  of the last unique element.
- Traverse the array using a read pointer.
- When a new (different) element is found, move it
  to the next write position.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Sorted order guarantees duplicates are adjacent.
- Each unique element is written exactly once.
- In-place modification avoids extra memory.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(n) → single pass through the array

Space Complexity:
- O(1) → constant extra space

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- This is a classic TWO POINTER problem.
- Sorting is NOT required (already sorted).
- Common mistake: using extra data structures.
- Interviewers expect O(1) space.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array
- Array with all elements same
- Array with no duplicates
- Single element array

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def removeDuplicates(nums):
    """
    Removes duplicates from a sorted array in-place.

    Parameters:
    nums (list): Sorted list of integers

    Returns:
    int: Number of unique elements
    """

    # Edge case: empty array
    if len(nums) == 0:
        return 0

    # write_index points to the last unique element position
    write_index = 0

    # Traverse array starting from second element
    for read_index in range(1, len(nums)):

        # If current element is different from last unique element
        if nums[read_index] != nums[write_index]:

            # Move write_index forward
            write_index += 1

            # Place the new unique element
            nums[write_index] = nums[read_index]

    # Number of unique elements
    return write_index + 1


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input
    nums = [1, 1, 2, 2, 3]

    print("Original array:", nums)

    # Remove duplicates
    k = removeDuplicates(nums)

    print("\nNumber of unique elements:", k)
    print("Modified array (first k elements are valid):", nums[:k])
