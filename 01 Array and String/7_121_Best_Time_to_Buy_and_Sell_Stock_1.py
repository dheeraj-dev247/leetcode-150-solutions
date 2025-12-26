"""
121. BEST TIME TO BUY AND SELL STOCK - DETAILED NOTES + CODE (PYTHON)

------------------------------------------------
PROBLEM STATEMENT:
------------------------------------------------
You are given an array prices where prices[i] is the price
of a given stock on the i-th day.

- You want to maximize your profit.
- You may complete at most ONE transaction
  (buy one and sell one share of the stock).
- You must buy before you sell.
- If no profit is possible, return 0.

------------------------------------------------
APPROACH 1: BRUTE FORCE
------------------------------------------------
INTUITION:
- Try every possible pair of buy day and sell day.
- Calculate profit for each valid pair.
- Track the maximum profit.

WHY IT WORKS:
- Directly checks all possible transactions.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n²)
- Space: O(1)

INTERVIEW NOTE:
- Easy to think of.
- Too slow for large inputs.

------------------------------------------------
APPROACH 2: BETTER (TRACK MIN PRICE)
------------------------------------------------
INTUITION:
- Traverse the array once.
- Keep track of the minimum price seen so far.
- At each step, calculate profit if sold today.
- Update maximum profit accordingly.

WHY IT WORKS:
- Best buying day is always the minimum price before today.
- Each day is considered as a selling day.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- This is the EXPECTED optimal solution.
- Simple and very commonly asked.

------------------------------------------------
APPROACH 3: OPTIMAL (KADANE'S ALGORITHM VIEW)
------------------------------------------------
INTUITION:
- Convert prices into daily profit differences.
- Find the maximum subarray sum (Kadane's Algorithm).

WHY IT WORKS:
- Buying at lowest point and selling at highest point after
  it gives maximum profit.
- Kadane naturally captures this behavior.

TIME AND SPACE COMPLEXITY:
------------------------------------------------
- Time: O(n)
- Space: O(1)

INTERVIEW NOTE:
- Useful for explanation depth.
- Not required to implement separately.

------------------------------------------------
IMPLEMENTATIONS BELOW:
------------------------------------------------
"""


# ------------------------------------------------
# BRUTE FORCE SOLUTION
# ------------------------------------------------
def maxProfit_bruteforce(prices):
    n = len(prices)
    max_profit = 0

    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)

    return max_profit


# ------------------------------------------------
# BETTER / OPTIMAL SOLUTION
# ------------------------------------------------
def maxProfit(prices):
    """
    Finds the maximum profit with one buy and one sell.

    Parameters:
    prices (list): Stock prices by day

    Returns:
    int: Maximum profit
    """

    min_price = float("inf")
    max_profit = 0

    for price in prices:

        # Update minimum price so far
        if price < min_price:
            min_price = price

        # Calculate profit if sold today
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit


# ------------------------------------------------
# DRIVER CODE (FOR TESTING)
# ------------------------------------------------
if __name__ == "__main__":

    prices = [7, 1, 5, 3, 6, 4]

    print("Stock prices:", prices)

    print("\nBrute Force Result:", maxProfit_bruteforce(prices))

    print("Optimal Result:", maxProfit(prices))
