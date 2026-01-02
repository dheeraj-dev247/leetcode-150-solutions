"""
27. REMOVE ELEMENT - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an integer array nums and an integer val,
remove all occurrences of val in nums IN-PLACE.

- The relative order of elements may be changed.
- Return the number of elements remaining after removal.
- It does NOT matter what values are left beyond the
  returned length.

------------------------------------------------
APPROACH (INTUITION):
------------------------------------------------
- Use a TWO POINTER technique.
- One pointer (write index) keeps track of the position
  where the next valid element should be placed.
- Traverse the array using a read pointer.
- Whenever the current element is NOT equal to val,
  place it at the write index and increment write index.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- All valid elements are compacted at the start of the array.
- In-place modification avoids extra space usage.
- The write pointer ensures only valid elements are kept.

------------------------------------------------
TIME AND SPACE COMPLEXITY:
------------------------------------------------
Time Complexity:
- O(n) → each element is checked once

Space Complexity:
- O(1) → constant extra space

------------------------------------------------
IMPORTANT INTERVIEW NOTES:
------------------------------------------------
- This problem tests in-place array manipulation.
- Order preservation is optional but this solution preserves it.
- Do NOT use extra arrays (unless explicitly allowed).

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Empty array
- Array with all elements equal to val
- Array with no occurrences of val
- Single element array

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def removeElement(nums, val):
    """
    Removes all occurrences of val in nums in-place.

    Parameters:
    nums (list): List of integers
    val (int): Value to remove

    Returns:
    int: Number of elements remaining after removal
    """

    # Pointer to track position for valid elements
    write_index = 0

    # Traverse the array
    for read_index in range(len(nums)):

        # If current element is not equal to val
        if nums[read_index] != val:

            # Place it at the write_index
            nums[write_index] = nums[read_index]

            # Move write_index forward
            write_index += 1

    # write_index is the count of valid elements
    return write_index


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input
    nums = [3, 2, 2, 3]
    val = 3

    print("Original array:", nums)
    print("Value to remove:", val)

    # Remove element
    k = removeElement(nums, val)

    print("\nNumber of elements after removal:", k)
    print("Modified array (first k elements are valid):", nums[:k])
