"""
Add all
Source: UVa   Time Limit: 3000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue

if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            exit(0)
        arr = map(int, input().split())
        pq = PriorityQueue()
        for i in arr:
            pq.put(i)
        cost = 0
        while len(pq.queue) > 0:
            v1 = pq.get()
            v2 = 0 if len(pq.queue) == 0 else pq.get()
            cost += v1 + v2
            if len(pq.queue) > 0:
                pq.put(v1 + v2)
        print(cost)
