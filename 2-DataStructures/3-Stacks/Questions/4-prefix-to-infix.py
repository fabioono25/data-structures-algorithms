# infix expression is the expression where the operator is in between the operands
# example: 1 + 2 + 3
# prefix expression is the expression where the operator is before the operands
# example: + 1 2 3
# postfix expression is the expression where the operator is after the operands
# example: 1 2 + 3 +

# convert a prefix expression to an infix expression
# example: *+AB-CD -> (A+B)*(C-D)
# example: *-A/BC-/AKL -> ((A-(B/C))*((A/K)-L))

def prefixToInfix(str):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for i in range(len(str)-1, -1, -1):
        if str[i] in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            temp = '(' + op1 + str[i] + op2 + ')'
            stack.append(temp)
        else:
            stack.append(str[i])

    return stack.pop()


if __name__ == "__main__":
    str = "*+AB-CD"
    print("Input: ", str, "- Output: ", prefixToInfix(str))

    str = "*-A/BC-/AKL"
    print("Input: ", str, "- Output: ", prefixToInfix(str))
