"""
Energy Exchange
Source: Codeforces   Time Limit: 2000ms   Memory Limit: 256MB
"""


def binarySearch(arr, value, left, right):
    if left >= right:
        return -1
    md = left + (right-left)//2
    if arr[md] >= value and (md == left or arr[md-1] < value):
        return md
    if arr[md] < value:
        return binarySearch(arr, value, md + 1, right)
    return binarySearch(arr, value, left, md)


if __name__ == "__main__":
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arrSum = list(arr)
    for i in range(1,n):
        arrSum[i] += arrSum[i-1]
    minValue, maxValue = arr[0], arr[-1]
    while True:
        value = minValue + (maxValue - minValue)/2
        index = binarySearch(arr, value, 0, n)
        sumChange = 0 if index == 0 else arrSum[-1] - value * (n - index) - arrSum[index-1]
        sumTransfer = sumChange * (100 - k)/100
        costValue = 0 if index == 0 else value * index - arrSum[index-1]
        st = sumTransfer - costValue
        if 0 <= st <= 10**-10:
            print("{:.9f}".format(value))
            break
        # st > 10 ** -10 --> tang value
        minValue, maxValue = (value, maxValue) if st > 10**-10 else (minValue, value)