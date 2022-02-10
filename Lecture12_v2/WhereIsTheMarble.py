"""
Where is the marble
Source: UVa   Time Limit: 2000ms   Memory Limit: 512MB
"""

def binarySearch(arr, value, left, right):
    if left >= right:
        return -1
    middle = left + (right - left)//2
    if arr[middle] == value and (middle == 0 or arr[middle-1] != value):
        return middle
    elif arr[middle] < value:
        return binarySearch(arr, value, middle + 1, right)
    return binarySearch(arr, value, left, middle)


def process(itc, n, q):
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    query = [int(input()) for _ in range(q)]
    print("CASE# {}:".format(itc))
    for v in query:
        index = binarySearch(arr, v, 0, n)
        if index == -1:
            print("{} not found".format(v))
        else:
            print("{} found at {}".format(v, index + 1))


if __name__ == "__main__":
    iTC = 1
    while True:
        n,q = map(int, input().split())
        if n == q == 0:
            exit(0)
        process(iTC, n, q)
        iTC += 1