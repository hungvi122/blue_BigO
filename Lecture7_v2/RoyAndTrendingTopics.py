"""
Roy and trending topics
Source: Hackerearth   Time Limit: 3000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue

if __name__ == "__main__":
    n = int(input())
    pQueue = PriorityQueue()

    for _ in range(n):
        id, zscore, topic, like, comment, share = map(int, input().split())
        nscore = topic * 50 + like * 5 + comment * 10 + share * 20
        increase = nscore - zscore
        pQueue.put((-increase, -id, nscore))

    for _ in range(5):
        increase, id, nscore = pQueue.get()
        print(-id, nscore)