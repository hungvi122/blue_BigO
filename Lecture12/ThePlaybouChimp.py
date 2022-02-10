"""
The Playboy chimp
Source: UVa   Time Limit: 1000ms   Memory Limit: 512MB
"""


# -1 check left, 1 check right, 0 return
def checkFunctionMaxLessThan(arr, value, middle, left, right):
    if arr[middle] < value and (middle == right - 1 or arr[middle + 1] >= value):
        return 0
    if arr[middle] >= value:
        return -1
    return 1


def checkFunctionMinGreatThan(arr, value, middle, left, right):
    if arr[middle] > value and (middle == left or arr[middle - 1] <= value):
        return 0
    if arr[middle] <= value:
        return 1
    return -1


def binarySearch(arr, value, left, right, checkFunction):
    if left >= right:
        return -1
    middle = left + (right - left)//2
    st = checkFunction(arr, value, middle, left, right)
    if st == 0:
        return middle
    elif st == -1:
        return binarySearch(arr, value, left, middle, checkFunction)
    return binarySearch(arr, value, middle + 1, right, checkFunction)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    queries = list(map(int, input().split()))
    for t in queries:
        indexMax = binarySearch(arr, t, 0, n, checkFunctionMaxLessThan)
        indexMin = binarySearch(arr, t, 0, n, checkFunctionMinGreatThan)
        x = arr[indexMax] if indexMax >= 0 else 'X'
        y = arr[indexMin] if indexMin >= 0 else 'X'
        print(x, y)