"""
Find the median
Source: Secret   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
from heapq import heappop, heappush

if __name__ == "__main__":
    n = int(input())
    maxHeap = []
    minHeap = []
    arr = map(int, input().split())
    index = 1
    for value in arr:
        heappush(minHeap, value)
        if index % 2 == 0:
            heappush(maxHeap, -heappop(minHeap))
        elif len(maxHeap) > 0 and -maxHeap[0] > minHeap[0]:
            vMinHeap, vMaxHeap = heappop(minHeap), -heappop(maxHeap)
            heappush(minHeap, vMaxHeap)
            heappush(maxHeap, -vMinHeap)

        index += 1
    print(minHeap[0])