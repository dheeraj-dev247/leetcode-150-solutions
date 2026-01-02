88. MERGE SORTED ARRAY - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given two integer arrays nums1 and nums2, sorted in
non-decreasing order, and two integers m and n representing
the number of elements in nums1 and nums2 respectively.

Merge nums2 into nums1 as one sorted array.

IMPORTANT:
- nums1 has a length of m + n
- The last n elements of nums1 are set to 0 and should be ignored
- You must modify nums1 in-place

------------------------------------------------
CORE IDEA (KEY OBSERVATION):
------------------------------------------------
Since nums1 has extra space at the END, we can merge the arrays
from RIGHT TO LEFT to avoid overwriting useful values.

Instead of shifting elements forward (costly),
we place the largest remaining element at the end.

------------------------------------------------
APPROACH 1: BRUTE FORCE (EXTRA SPACE)
------------------------------------------------
INTUITION:
- Copy elements of nums1 (first m elements) and nums2 into a new array.
- Sort the new array.
- Copy elements back into nums1.

WHY IT WORKS:
- Sorting guarantees correct order.

DRAWBACK:
- Uses extra space.
- Not optimal and usually NOT expected in interviews.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O((m + n) log(m + n))
- Space: O(m + n)

INTERVIEW NOTE:
- Correct but inefficient.
- Avoid unless explicitly allowed extra space.

------------------------------------------------
APPROACH 2: BETTER (USING TEMP ARRAY, TWO POINTERS)
------------------------------------------------
INTUITION:
- Use two pointers to merge like the merge step of merge sort.
- Store result in a temporary array.
- Copy merged result back to nums1.

WHY IT WORKS:
- Both arrays are already sorted.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(m + n)
- Space: O(m + n)

INTERVIEW NOTE:
- Good logic, but still not in-place.
- Interviewers usually push for better.

------------------------------------------------
APPROACH 3: OPTIMAL (IN-PLACE, THREE POINTERS FROM BACK)
------------------------------------------------
INTUITION:
- Use three pointers:
  - i → last valid element in nums1 (m - 1)
  - j → last element in nums2 (n - 1)
  - k → last position in nums1 (m + n - 1)
- Compare nums1[i] and nums2[j]
- Place the larger value at nums1[k]
- Move pointers accordingly

WHY THIS WORKS (IMPORTANT):
------------------------------------------------
- nums1 has extra space at the end.
- Filling from the back avoids overwriting elements
  that are still needed for comparison.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(m + n)
- Space: O(1)

INTERVIEW NOTE:
- EXPECTED solution.
- Very common array manipulation problem.
- Tests understanding of in-place operations.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- nums2 is empty (n = 0)
- nums1 has no valid elements (m = 0)
- All elements of nums2 are smaller than nums1
- All elements of nums2 are larger than nums1

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
