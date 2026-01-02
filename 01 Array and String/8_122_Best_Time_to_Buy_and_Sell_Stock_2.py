"""
122. BEST TIME TO BUY AND SELL STOCK II - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given an array prices where prices[i] is the price
of a given stock on the i-th day.

- You may complete as many transactions as you like
  (buy one and sell one share multiple times).
- You may NOT hold multiple stocks at the same time.
- You must sell before buying again.
- Return the maximum profit.

------------------------------------------------
APPROACH 1: BRUTE FORCE (RECURSION)
------------------------------------------------
INTUITION:
- At each day, decide to buy, sell, or skip.
- Explore all possible combinations.

WHY IT WORKS:
- Considers all valid transaction sequences.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: Exponential (2^n)
- Space: O(n) recursion stack

INTERVIEW NOTE:
- Not practical.
- Used only to explain thought process.

------------------------------------------------
APPROACH 2: BETTER (PEAK-VALLEY APPROACH)
------------------------------------------------
INTUITION:
- Buy at every local minimum (valley).
- Sell at every local maximum (peak).
- Sum all profits from each transaction.

WHY IT WORKS:
- Any increasing sequence can be broken into
  multiple profitable transactions.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- Conceptually helpful.
- Slightly more complex to code.

------------------------------------------------
APPROACH 3: OPTIMAL (GREEDY)
------------------------------------------------
INTUITION:
- Whenever today’s price is higher than yesterday’s,
  take the profit.
- Sum all positive differences.

WHY IT WORKS:
- Captures all upward movements.
- Equivalent to buying before every rise and selling at the top.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- MOST EXPECTED solution.
- Simple and elegant.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION (RECURSION)
# ------------------------------------------------
def maxProfit_bruteforce(prices):

    def dfs(index, holding):
        if index == len(prices):
            return 0

        # Skip
        profit = dfs(index + 1, holding)

        if holding:
            # Sell
            profit = max(profit, prices[index] + dfs(index + 1, False))
        else:
            # Buy
            profit = max(profit, -prices[index] + dfs(index + 1, True))

        return profit

    return dfs(0, False)


# ------------------------------------------------
# BETTER SOLUTION (PEAK-VALLEY)
# ------------------------------------------------
def maxProfit_better(prices):
    n = len(prices)
    i = 0
    profit = 0

    while i < n - 1:
        # Find valley
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        buy = prices[i]

        # Find peak
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        sell = prices[i]

        profit += sell - buy

    return profit


# ------------------------------------------------
# OPTIMAL SOLUTION (GREEDY)
# ------------------------------------------------
def maxProfit(prices):
    total_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]

    return total_profit


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    prices = [7, 1, 5, 3, 6, 4]

    print("Stock prices:", prices)

    print("\nBrute Force Result:", maxProfit_bruteforce(prices))

    print("Better (Peak-Valley) Result:", maxProfit_better(prices))

    print("Optimal (Greedy) Result:", maxProfit(prices))
