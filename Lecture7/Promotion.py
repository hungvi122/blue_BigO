"""
Promotion
Source: SPOJ   Time Limit: 1500ms   Memory Limit: 512MB
"""
from queue import PriorityQueue

if __name__ == "__main__":
    n = int(input())
    arrCount = [0] * (10 ** 6 + 1)
    pqMax = PriorityQueue()
    pqMin = PriorityQueue()
    sumTotal = 0
    for _ in range(n):
        arr = map(int, input().split()[1:])
        for i in arr:
            if i > 0:
                arrCount[i] += 1
                pqMin.put(i)
                pqMax.put(-i)
        mMin, mMax = 0, 0

        while True:
            mMax = -pqMax.get()
            if arrCount[mMax] > 0:
                arrCount[mMax] -= 1
                break
        while True:
            mMin = pqMin.get()
            if arrCount[mMin] > 0:
                arrCount[mMin] -= 1
                break

        sumTotal += mMax - mMin
    print(sumTotal)