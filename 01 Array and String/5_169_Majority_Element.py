"""
169. MAJORITY ELEMENT - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array nums of size n, return the majority element.

- The majority element is the element that appears
  more than ⌊ n / 2 ⌋ times.
- You may assume that the majority element always exists.

------------------------------------------------
APPROACH 1: BRUTE FORCE
------------------------------------------------
INTUITION:
- For every element, count how many times it appears.
- If its count exceeds n/2, return it.

WHY IT WORKS:
- Directly checks the definition of majority element.

TIME AND SPACE COMPLEXITY:
- Time: O(n²)
- Space: O(1)

INTERVIEW NOTE:
- Simple but inefficient.
- Usually NOT accepted in interviews.

------------------------------------------------
APPROACH 2: BETTER (HASH MAP)
------------------------------------------------
INTUITION:
- Use a hash map to store frequency of each element.
- While counting, if frequency exceeds n/2, return it.

WHY IT WORKS:
- Counting frequencies gives exact occurrences.

TIME AND SPACE COMPLEXITY:
- Time: O(n)
- Space: O(n)

INTERVIEW NOTE:
- Acceptable solution.
- Not optimal due to extra space.

------------------------------------------------
APPROACH 3: OPTIMAL (BOYER-MOORE VOTING)
------------------------------------------------
INTUITION:
- Use pair cancellation.
- Maintain a candidate and a count.
- When count reaches 0, select a new candidate.
- Majority element cannot be fully canceled.

WHY IT WORKS:
- Majority element appears more than n/2 times.
- After all cancellations, it must remain.

TIME AND SPACE COMPLEXITY:
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- MOST IMPORTANT solution.
- Expected by interviewers.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def majorityElement_bruteforce(nums):
    n = len(nums)

    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1

        if count > n // 2:
            return nums[i]


# ------------------------------------------------
# BETTER SOLUTION (HASH MAP)
# ------------------------------------------------
def majorityElement_better(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

        if freq[num] > len(nums) // 2:
            return num


# ------------------------------------------------
# OPTIMAL SOLUTION (BOYER-MOORE)
# ------------------------------------------------
def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    nums = [2, 2, 1, 1, 1, 2, 2]

    print("Array:", nums)

    print("\nBrute Force Result:", majorityElement_bruteforce(nums))

    print("Better (HashMap) Result:", majorityElement_better(nums))

    print("Optimal (Boyer-Moore) Result:", majorityElement(nums))
