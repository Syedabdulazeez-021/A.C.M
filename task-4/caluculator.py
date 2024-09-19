def parse_expression(expression):
    def helper(expr, index):
        num = 0
        stack = []
        sign = 1
        result = 0

        while index < len(expr):
            char = expr[index]

            if char.isdigit():
                num = 0
                while index < len(expr) and expr[index].isdigit():
                    num = num * 10 + int(expr[index])
                    index += 1
                result += sign * num
                continue

            if char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            elif char == '(':
                num, index = helper(expr, index + 1)
                result += sign * num
            elif char == ')':
                return result, index
            elif char in '*/':
                index += 1
                num = 0
                while index < len(expr) and expr[index].isdigit():
                    num = num * 10 + int(expr[index])
                    index += 1
                if char == '*':
                    result *= num
                elif char == '/':
                    if num != 0:
                        result //= num
                    else:
                        return "Error: Division by zero.", index
                continue

            index += 1

        return result, index

    result, _ = helper(expression, 0)
    return result

print("Simple Calculator")
print("Enter a mathematical expression using integers and operators (+, -, *, /).")

expression = input("Enter expression: ")
expression = expression.replace(" ", "")
print(f"Expression: {expression}")

result = parse_expression(expression)
print(f"Result: {result}")
