"""
274. H-INDEX - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Given an array citations where citations[i] is the number of
citations a researcher received for their i-th paper,
return the researcher's h-index.

Definition:
- The h-index is the maximum value h such that the researcher
  has at least h papers with at least h citations each.

------------------------------------------------
APPROACH 1: BRUTE FORCE
------------------------------------------------
INTUITION:
- Try every possible value of h from 1 to n.
- For each h, count how many papers have citations >= h.
- If count >= h, it is a valid h-index.
- Return the maximum valid h.

WHY IT WORKS:
- Directly follows the definition of h-index.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n²)
- Space: O(1)

INTERVIEW NOTE:
- Easy to reason about.
- Inefficient for large inputs.

------------------------------------------------
APPROACH 2: BETTER (SORTING)
------------------------------------------------
INTUITION:
- Sort the citations in ascending order.
- For each index i, check how many papers have citations
  >= citations[i].
- If (n - i) >= citations[i], update h-index.

WHY IT WORKS:
- Sorting lets us know how many papers lie to the right.
- We efficiently test the h-index condition.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n log n)
- Space: O(1) or O(n) depending on sort implementation

INTERVIEW NOTE:
- Very common accepted solution.
- Good balance between simplicity and efficiency.

------------------------------------------------
APPROACH 3: OPTIMAL (COUNTING / BUCKET SORT)
------------------------------------------------
INTUITION:
- h-index can never exceed n (number of papers).
- Count how many papers have each citation count.
- Group all citations >= n into one bucket.
- Traverse buckets from high to low, accumulating counts.
- The first h where accumulated count >= h is the answer.

WHY IT WORKS:
- We only care about citation counts up to n.
- Counting avoids sorting and achieves linear time.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(n)

INTERVIEW NOTE:
- Optimal solution.
- Very impressive if explained clearly.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def hIndex_bruteforce(citations):
    n = len(citations)
    h_index = 0

    # if we go till n then n will be excluded so we go till n+1
    for h in range(1, n + 1):
        count = 0
        for c in citations:
            if c >= h:
                count += 1
        if count >= h:
            h_index = h

    return h_index


# ------------------------------------------------
# BETTER SOLUTION (SORTING)
# ------------------------------------------------
def hIndex_sorting(citations):
    citations.sort()
    n = len(citations)
    h_index = 0

    for i in range(n):
        # papers with citations >= citations[i]
        papers = n - i
        if citations[i] >= papers:
            h_index = max(h_index, papers)

    return h_index


# ------------------------------------------------
# OPTIMAL SOLUTION (COUNTING / BUCKET)
# ------------------------------------------------
def hIndex(citations):
    """
    Computes the h-index using counting method.

    Parameters:
    citations (list): List of citation counts

    Returns:
    int: h-index
    """

    n = len(citations)

    # Buckets from 0 to n
    buckets = [0] * (n + 1)

    # Count citations
    for c in citations:
        if c >= n:
            buckets[n] += 1
        else:
            buckets[c] += 1

    total_papers = 0

    # Traverse from high to low
    for h in range(n, -1, -1):
        total_papers += buckets[h]
        if total_papers >= h:
            return h

    return 0


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    citations = [3, 0, 6, 1, 5]

    print("Citations:", citations)

    print("\nBrute Force Result:", hIndex_bruteforce(citations))

    print("Better (Sorting) Result:", hIndex_sorting(citations.copy()))

    print("Optimal (Counting) Result:", hIndex(citations))
