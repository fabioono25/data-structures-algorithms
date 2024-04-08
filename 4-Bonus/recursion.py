# recursion example

def findFactorialRecursive(number):
    if number == 2:
        return 2
    return number * findFactorialRecursive(number - 1)

# solving factorial using iteration
def findFactorialIterative(number):
    answer = 1
    for i in range(2, number + 1):
        answer *= i
    return answer

# solving factorial with memoization
def findFactorialMemoization(number, memo={}):
    if number in memo:
        return memo[number]
    if number == 2:
        return 2
    memo[number] = number * findFactorialMemoization(number - 1, memo)
    return memo[number]

def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# solving fibonacci using iteration
def fibonacci_iterative(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
  
# solving fibonacci with memoization
def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]  
  
# testing all functions
print(findFactorialRecursive(5))  # 120
print(findFactorialIterative(5))  # 120
print(findFactorialMemoization(5))  # 120
print(fibonacci_recursive(10))  # 55
print(fibonacci_iterative(10))  # 55
print(fibonacci_memoization(10))  # 55