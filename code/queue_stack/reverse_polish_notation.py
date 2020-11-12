## LC 150

## Input: ["2", "1", "+", "3", "*"]
## Output: 9
## Explanation: ((2 + 1) * 3) = 9

def reverse_polish_notation(tokens):
    stack = []

    for num in tokens:
        if num == "+":
            num2 = stack.pop()
            num1 = stack.pop()
            result = num1 + num2
            stack.append(result)
        elif num == "-":
            num2 = stack.pop()
            num1 = stack.pop()
            result = num1 - num2
            stack.append(result)
        elif num == "*":
            num2 = stack.pop()
            num1 = stack.pop()
            result = num1 * num2
            stack.append(result)
        elif num == "/":
            sign = 1
            num2 = stack.pop()
            num1 = stack.pop()
            if num1 * num2 < 0:  ### 在python3里，3 // -5 = -1, 但是题目要求 3 // -5 = 0
                sign = -1
            
            result = sign * (abs(num1) // abs(num2))
            stack.append(result)
        else:
            stack.append(int(num))
    return stack[-1]