"""
Monk and multiplication
Source: Hackerearth   Time Limit: 1000ms   Memory Limit: 256MB
5
1 2 3 4 5
"""
from queue import PriorityQueue

if __name__ == "__main__":
    n = int(input())
    pqQueue = PriorityQueue()
    arr = list(map(int, input().split()))
    for i in range(n):
        pqQueue.put(-arr[i])
        if i < 2:
            print(-1)
        else:
            t1 = -pqQueue.get()
            t2 = -pqQueue.get()
            t3 = -pqQueue.get()
            print(t1 * t2 * t3)
            pqQueue.put(-t1)
            pqQueue.put(-t2)
            pqQueue.put(-t3)

