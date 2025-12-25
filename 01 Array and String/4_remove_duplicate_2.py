"""
80. REMOVE DUPLICATES FROM SORTED ARRAY II - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given a sorted integer array nums, remove duplicates IN-PLACE
such that each unique element appears at most TWICE.

- The relative order of the elements should be preserved.
- Return the number of elements after removal.
- Do NOT use extra space for another array.
- Modify nums in-place.

------------------------------------------------
APPROACH (INTUITION):
------------------------------------------------
- Since the array is sorted, duplicates are adjacent.
- We can allow at most two occurrences of each number.
- Use a TWO POINTER technique.
- One pointer (write index) tracks where the next valid
  element should be placed.
- Traverse the array with a read pointer.
- Compare the current element with the element two positions
  before the write index to decide if it can be kept.

------------------------------------------------
WHY THIS APPROACH WORKS:
------------------------------------------------
- Sorted order ensures duplicates are grouped together.
- By checking nums[write_index - 2], we guarantee that no
  element appears more than twice.
- In-place modification keeps space usage minimal.

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
- This is an extension of LeetCode 26.
- Key trick: compare with element at (write_index - 2).
- Interviewers expect this O(1) space solution.
- Returning write_index gives the new length.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Array length <= 2 → always valid as-is
- Array with all same elements
- Array with no duplicates
- Large arrays

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""


def removeDuplicates(nums):
    """
    Removes duplicates such that each element appears at most twice.

    Parameters:
    nums (list): Sorted list of integers

    Returns:
    int: Length of array after removing extra duplicates
    """

    # Arrays with 2 or fewer elements are always valid
    if len(nums) <= 2:
        return len(nums)

    # write_index points to where the next valid element goes
    write_index = 2

    # Traverse starting from the third element
    for read_index in range(2, len(nums)):

        # Check if current element can be kept
        if nums[read_index] != nums[write_index - 2]:

            nums[write_index] = nums[read_index]
            write_index += 1

    # write_index represents the new length
    return write_index


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    # Example input
    nums = [1, 1, 1, 2, 2, 3]

    print("Original array:", nums)

    # Remove extra duplicates
    k = removeDuplicates(nums)

    print("\nNumber of elements after removal:", k)
    print("Modified array (first k elements are valid):", nums[:k])
