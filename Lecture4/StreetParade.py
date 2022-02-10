"""
Street Parade
Source: Spoj   Time Limit: 1000ms   Memory Limit: 512MB
5
5 1 2 4 3
0
"""


def process(n):
    arr = list(map(int, input().split()))
    stack = []
    number, index = 1, 0
    while index < len(arr):
        if arr[index] == number:
            index += 1
            number += 1
        elif len(stack) > 0 and stack[-1] == number:
            stack.pop()
            number += 1
        else:
            if len(stack) > 0 and stack[-1] < arr[index]:
                return False
            else:
                stack.append(arr[index])
                index += 1
    return True


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            exit(0)
        result = process(n)
        if result:
            print("yes")
        else:
            print("no")