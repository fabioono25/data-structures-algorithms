# recursion example

def findFactorialRecursive(number):
    if number == 2:
        return 2
    return number * findFactorialRecursive(number - 1)

def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
