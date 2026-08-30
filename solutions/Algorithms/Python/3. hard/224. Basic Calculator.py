
def calculate(s):
    stack = []
    operand = 0
    result = 0 
    sign = 1  
    for char in s:
        if char.isdigit():
            operand = operand * 10 + int(char)
        elif char == '+':
            result += sign * operand
            sign = 1
            operand = 0
        elif char == '-':
            result += sign * operand
            sign = -1
            operand = 0
        elif char == '(':
            stack.append((result, sign))
            result, sign = 0, 1
        elif char == ')':
            result += sign * operand
            prev_result, prev_sign = stack.pop()
            result = prev_result + prev_sign * result
            operand = 0

    return result + sign * operand





print(calculate("(1+(4+5+2)-3)+(6+8)"))
print(calculate("1 + 1"))
print(calculate("123"))