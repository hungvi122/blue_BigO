"""
Compilers And Parsers
Source: Codechef   Time Limit: 1000ms   Memory Limit: 512MB

3
<<>>
><
<>>>
"""

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        expression = input()
        count, stack = 0, []

        for i in range(len(expression)):
            ch = expression[i]
            if ch == '<':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    break
                stack.pop()
                if len(stack) == 0:
                    count = i + 1
        print(count)