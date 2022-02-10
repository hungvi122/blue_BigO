"""
Pizzamania
Source: SPOJ   Time Limit: 3000ms   Memory Limit: 1024MB
"""

def binarySearch(arr, value, left, right):
    if left >= right:
        return -1
    middle = left + (right - left)//2
    if arr[middle] == value:
        return middle
    elif arr[middle] > value:
        return binarySearch(arr, value, left, middle)
    return binarySearch(arr, value, middle + 1, right)


if __name__ == "__main__":
    itc = int(input())
    for _ in range(itc):
        n,m = map(int, input().split())
        arr = list(map(int, input().split()))
        arr.sort()
        count = 0
        for i in range(n):
            index = binarySearch(arr, m - arr[i], i + 1, n)
            if index >= 0:
                count += 1
        print(count)