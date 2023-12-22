# given an array for which the ith element is the price of a given stock on day i
# design an algorithm to find the maximum profit.
# ex: [7,1,5,3,6,4] -> 5 - Explanation: buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 5-1 = 4
# ex: [1,2,3,4,5] -> 4 - Explanation: buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4
# ex: [7,6,4,3,1] -> 0 - Explanation: no transaction is done, profit = 0

# Solution 1: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def maxProfit1(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


# Solution 2: One Pass
# Time Complexity: O(n)
# Space Complexity: O(1)
def maxProfit2(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

# Solution 3: Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)


def maxProfit3(prices):
    max_current = 0
    max_global = 0
    for i in range(1, len(prices)):
        max_current = max(0, max_current + prices[i] - prices[i-1])
        max_global = max(max_global, max_current)
    return max_global


# tests
prices = [7, 1, 5, 3, 6, 4]
print('Input: ', prices)
print('Solution 1: Brute Force')
print('Output: ', maxProfit1(prices))
print(25*'-')
print('Solution 2: One Pass')
print('Output: ', maxProfit2(prices))
print(25*'-')
print('Solution 3: Kadane\'s Algorithm')
print('Output: ', maxProfit3(prices))
print(25*'#')
prices = [1, 2, 3, 4, 5]
print('Input: ', prices)
print('Solution 1: Brute Force')
print('Output: ', maxProfit1(prices))
print(25*'-')
print('Solution 2: One Pass')
print('Output: ', maxProfit2(prices))
print(25*'-')
print('Solution 3: Kadane\'s Algorithm')
print('Output: ', maxProfit3(prices))
print(25*'#')
prices = [7, 6, 4, 3, 1]
print('Input: ', prices)
print('Solution 1: Brute Force')
print('Output: ', maxProfit1(prices))
print(25*'-')
print('Solution 2: One Pass')
print('Output: ', maxProfit2(prices))
print(25*'-')
print('Solution 3: Kadane\'s Algorithm')
print('Output: ', maxProfit3(prices))
print(25*'#')
