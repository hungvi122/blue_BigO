"""
Restaurant Rating
Source: Codechef   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue

if __name__ == "__main__":
    n = int(input())
    pqMax = PriorityQueue()
    pqMin = PriorityQueue()
    for i in range(n):
        params = input().split()
        if len(params) == 2:
            c = int(params[1])
            pqMax.put(-c)
            if (len(pqMin.queue) + len(pqMax.queue)) % 3 == 0:
                u = pqMax.get()
                pqMin.put(-u)
            elif len(pqMin.queue) > 0:
                topMin, topMax = pqMin.queue[0], - pqMax.queue[0]
                if topMin < topMax:
                    pqMax.put(-pqMin.get())
                    pqMin.put(-pqMax.get())
        else:
            if len(pqMin.queue) > 0:
                print(pqMin.queue[0])
            else:
                print("No reviews yet")

