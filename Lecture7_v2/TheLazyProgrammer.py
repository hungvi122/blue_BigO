"""
The Lazy Programmer
Source: SPOJ   Time Limit: 1500ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
def process():
    n = int(input())
    pQueue = PriorityQueue()
    for _ in range(n):
        a,b,d = map(int, input().split())
        pQueue.put((d,a,b))
    cost = 0
    time = 0
    pQueueMin = PriorityQueue()
    while len(pQueue.queue) > 0:
        d, a, b = pQueue.get()
        pQueueMin.put([-a, b])
        needTime = b + time - d
        if needTime < 0:
            time += b
        else:
            time = d
            while True:
                f, t = pQueueMin.get()
                if t > needTime:
                    t -= needTime
                    cost += needTime/-f
                    pQueueMin.put([f, t])
                    break
                else:
                    needTime -= t
                    cost += t/-f
    print("{:.2f}".format(cost))


if __name__ == "__main__":
    iTC = int(input())
    for _ in range(iTC):
        process()