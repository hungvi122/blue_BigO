"""
Hacking the random number generator
Source: SPOJ   Time Limit: 1000ms   Memory Limit: 512MB
"""

def binarySearch(arr, value, left, right):
    if left >= right:
        return -1
    middle = left + (right-left)//2
    if arr[middle] == value:
        return middle
    if arr[middle] < value:
        return binarySearch(arr, value, middle + 1, right)
    return binarySearch(arr, value, left, middle)


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    for i in range(n):
        index = binarySearch(arr, k + arr[i], i + 1, n)
        if index > i:
            count += 1
    print(count)