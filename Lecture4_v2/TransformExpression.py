"""
Transform the Expression
Nguồn bài: Spoj   Giới hạn thời gian: 1000ms   Giới hạn bộ nhớ: 512MB

"""
mapOperation = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
def tranformRPN(expression):
    stack = []
    result_tranform = ""
    for ch in expression:
        if 'a' <= ch <= 'z':
            result_tranform += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                result_tranform += stack.pop()
            stack.pop()
        else:
            while len(stack) > 0 and mapOperation.get(stack[-1]) > mapOperation.get(ch):
                result_tranform += stack.pop()
            stack.append(ch)
    while len(stack) > 0:
        result_tranform += stack.pop()
    return result_tranform


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        expression = input()
        result = tranformRPN(expression)
        print(result)
