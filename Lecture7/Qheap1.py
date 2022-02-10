"""
Qheap 1
Source: Hackerrank   Time Limit: 1000ms   Memory Limit: 512MB
"""

from queue import PriorityQueue

if __name__ == "__main__":
    n = int(input())
    pq = PriorityQueue()
    pqq = PriorityQueue()
    for i in range(n):
        params = input().split()
        if len(params) > 1:
            u, v = map(int, params)
            if u == 1:
                pq.put(v)
            else:
                pqq.put(v)
        else:
            while True:
                is_empty = len(pqq.queue) == 0
                v = pq.get()
                v2 = 0 if is_empty else pqq.get()
                if is_empty or v != v2:
                    pq.put(v)
                    print(v)
                    if not is_empty:
                        pqq.put(v2)
                    break
