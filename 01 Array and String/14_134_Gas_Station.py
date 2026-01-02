"""
134. GAS STATION - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
There are n gas stations arranged in a circular route.
You are given two integer arrays:

- gas[i]: amount of gas at station i
- cost[i]: gas required to travel from station i to (i+1)

Return the starting gas station index if you can travel
around the circuit once in the clockwise direction.
Otherwise, return -1.

IMPORTANT:
- If a solution exists, it is UNIQUE.

------------------------------------------------
APPROACH 1: BRUTE FORCE
------------------------------------------------
INTUITION:
- Try starting from every gas station.
- Simulate the journey.
- If gas ever becomes negative, fail and try next station.

WHY IT WORKS:
- Directly checks all possible starting points.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n²)
- Space: O(1)

INTERVIEW NOTE:
- Easy to think of.
- Too slow for large inputs.

------------------------------------------------
APPROACH 2: OPTIMAL (GREEDY)
------------------------------------------------
INTUITION:
- If total gas < total cost → impossible (return -1).
- Traverse once, tracking current fuel.
- If fuel drops below 0 at index i:
  - Any station before i cannot be a valid start.
  - Reset start to i+1.
  - Reset current fuel to 0.

WHY THIS WORKS:
- A negative fuel at index i means the chosen start
  cannot reach station i.
- Since gas stations are circular, skipping all previous
  stations is safe.
- The station after failure is the next best candidate.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- VERY IMPORTANT greedy problem.
- Logic-based, not math-heavy.
- Interviewers expect this solution.

------------------------------------------------
EDGE CASES:
------------------------------------------------
- Single station
- Total gas exactly equals total cost
- Large arrays

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def canCompleteCircuit_bruteforce(gas, cost):
    n = len(gas)

    for start in range(n):
        fuel = 0
        possible = True

        for i in range(n):
            idx = (start + i) % n
            fuel += gas[idx] - cost[idx]

            if fuel < 0:
                possible = False
                break

        if possible:
            return start

    return -1


# ------------------------------------------------
# OPTIMAL SOLUTION (GREEDY)
# ------------------------------------------------
def canCompleteCircuit(gas, cost):
    """
    Returns the starting gas station index if possible,
    otherwise returns -1.

    Parameters:
    gas (list): Gas available at each station
    cost (list): Gas required to go to next station

    Returns:
    int: Starting index or -1
    """

    total_gas = 0
    current_gas = 0
    start_index = 0

    for i in range(len(gas)):
        diff = gas[i] - cost[i]

        total_gas += diff
        current_gas += diff

        # If current gas becomes negative, reset start
        if current_gas < 0:
            start_index = i + 1
            current_gas = 0

    # If total gas is negative, no solution exists
    if total_gas < 0:
        return -1

    return start_index


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    print("Gas:", gas)
    print("Cost:", cost)

    print("\nBrute Force Result:", canCompleteCircuit_bruteforce(gas, cost))

    print("Optimal (Greedy) Result:", canCompleteCircuit(gas, cost))
