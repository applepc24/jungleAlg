def print_gwalho(s):
    stack = []

    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    stack.append(2 if temp == 0 else 2 * temp)
                    break
                elif isinstance(top, int):
                    temp += top
                else:
                    return 0
            else:
                return 0  # 괄호 짝이 안 맞음
        elif char == ']':
            temp = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    stack.append(3 if temp == 0 else 3 * temp)
                    break
                elif isinstance(top, int):
                    temp += top
                else:
                    return 0
            else:
                return 0  # 괄호 짝이 안 맞음
        else:
            return 0  # 이상한 문자 들어오면

    result = 0
    for val in stack:
        if isinstance(val, int):
            result += val
        else:
            return 0  # 괄호가 남아 있으면 잘못된 수식

    return result

expr = input().strip()
print(print_gwalho(expr))
                