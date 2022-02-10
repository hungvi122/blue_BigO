"""
Eko
Source: SPOJ   Time Limit: 2000ms   Memory Limit: 512MB
"""


def binarySearch(arr, value, left, right):
    if left >= right:
        return -1
    middle = left + (right - left)//2
    if arr[middle] >= value and (middle == 0 or arr[middle-1] < value):
        return middle
    elif arr[middle] < value:
        return binarySearch(arr, value, middle + 1, right)
    return binarySearch(arr, value, left, middle)


if __name__ == "__main__":
    n,m = map(int, input().split())
    arr = [int(i) for i in input().split()]
    arr.sort()
    arrSum = list(arr)
    for i in range(1,n):
        arrSum[i] += arrSum[i-1]
    minValue, maxValue = 0, arr[-1]
    left, right = 0, n
    while True:
        value = minValue + (maxValue - minValue)//2
        index = binarySearch(arr, value, left, right)
        index2 = binarySearch(arr, value+1, index, right)
        sumValue = arrSum[-1] - value * (n-index) if index == 0 else arrSum[-1] - arrSum[index-1] - value * (n-index)
        sumValue2 = arrSum[-1] - (value+1) * (n-index2) if index2 == 0 else arrSum[-1] - arrSum[index2-1] - (value+1) * (n-index2)
        if sumValue >= m > sumValue2:
            print(value)
            exit(0)
        if sumValue > m:
            minValue, maxValue = value, maxValue
            left, right = index, right
        else:
            minValue, maxValue = minValue, value
            left, right = left, index+1
