"""
I Can Guess the Data Structure!
Source: UVA   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue

def process(n):
    sStack, qQueue, mPQ = [], [], PriorityQueue()
    marks = [1] * 3
    for _ in range(n):
        c, v = map(int, input().split())
        if c == 1:
            sStack.append(v)
            qQueue.append(v)
            mPQ.put(-v)
        else:
            if marks[0] == 1 and v != sStack.pop():
                marks[0] = 0
            if marks[1] == 1 and v != qQueue.pop(0):
                marks[1] = 0
            if marks[2] == 1 and v != -mPQ.get():
                marks[2] = 0
    s = sum(marks)
    if s == 0:
        print("impossible")
    elif s > 1:
        print("not sure")
    else:
        if marks[0] == 1:
            print("stack")
        elif marks[1] == 1:
            print("queue")
        else:
            print("priority queue")


if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            process(n)
        except EOFError:
            exit(0)
