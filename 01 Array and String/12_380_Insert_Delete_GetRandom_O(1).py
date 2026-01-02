"""
380. INSERT DELETE GETRANDOM O(1) - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
Design a data structure that supports the following operations
in AVERAGE O(1) time:

1. insert(val)   → Inserts an item val if not present
2. remove(val)   → Removes an item val if present
3. getRandom()   → Returns a random element from current set

Constraints:
- Each element must have equal probability of being returned.
- You may assume getRandom is called only when at least one
  element exists.

------------------------------------------------
WHY THIS PROBLEM IS IMPORTANT:
------------------------------------------------
- Tests understanding of O(1) operations
- Combines ARRAY + HASHMAP
- Very common FAANG interview problem
- Tests data structure design skills

------------------------------------------------
APPROACH 1: BRUTE FORCE (LIST ONLY)
------------------------------------------------
INTUITION:
- Use a list to store elements.
- Insert at end → O(1)
- getRandom → O(1)
- remove → O(n) (need to search and shift)

WHY IT FAILS:
- Removal is O(n), not acceptable.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Insert: O(1)
- Remove: O(n) ❌
- getRandom: O(1)
- Space: O(n)

INTERVIEW NOTE:
- Mention quickly, then reject.

------------------------------------------------
APPROACH 2: OPTIMAL (LIST + HASHMAP)
------------------------------------------------
INTUITION:
- Use a list to store values (for getRandom).
- Use a hashmap to store value → index in list.
- For deletion:
  - Swap element with last element in list.
  - Remove last element.
  - Update index in hashmap.

WHY THIS WORKS:
- List gives O(1) access and random selection.
- Hashmap gives O(1) lookup for index.
- Swap avoids costly shifting.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Insert: O(1)
- Remove: O(1)
- getRandom: O(1)
- Space: O(n)

INTERVIEW NOTE:
- THIS IS THE EXPECTED SOLUTION.
- Key trick: swap with last element during removal.

------------------------------------------------
IMPLEMENTATION BELOW:
------------------------------------------------
"""

import random


class RandomizedSet:
    """
    Data structure supporting insert, remove, and getRandom
    in average O(1) time.
    """

    def __init__(self):
        # List to store elements
        self.values = []

        # Hashmap to store value -> index mapping
        self.index_map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts val into the set if not present.

        Returns:
        bool: True if inserted, False if already present
        """

        # If value already exists
        if val in self.index_map:
            return False

        # Add value to list
        self.values.append(val)

        # Store index in hashmap
        self.index_map[val] = len(self.values) - 1

        return True

    def remove(self, val: int) -> bool:
        """
        Removes val from the set if present.

        Returns:
        bool: True if removed, False if not present
        """

        # If value does not exist
        if val not in self.index_map:
            return False

        # Index of element to remove
        remove_index = self.index_map[val]

        # Last element in list
        last_val = self.values[-1]

        # Move last element to remove_index
        self.values[remove_index] = last_val
        self.index_map[last_val] = remove_index

        # Remove last element
        self.values.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        """
        Returns a random element from the set.
        """

        return random.choice(self.values)


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    randomizedSet = RandomizedSet()

    print(randomizedSet.insert(1))  # True
    print(randomizedSet.remove(2))  # False
    print(randomizedSet.insert(2))  # True
    print(randomizedSet.getRandom())  # 1 or 2
    print(randomizedSet.remove(1))  # True
    print(randomizedSet.insert(2))  # False
    print(randomizedSet.getRandom())  # 2
