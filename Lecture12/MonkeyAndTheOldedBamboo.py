"""
Monkey and the oiled bamboo
Source: UVa   Time Limit: 3000ms   Memory Limit: 512MB
"""

if __name__ == "__main__":
    iTC = int(input())
    for tc in range(iTC):
        n = int(input())
        arr = list(map(int, input().split()))

        if n == 1:
            k = arr[0]
        else:
            k = arr[-1] - arr[-2]
            for i in range(n-2,0,-1):
                if arr[i] - arr[i-1] > k:
                    k = arr[i] - arr[i-1]
                elif arr[i] - arr[i-1] == k:
                    k += 1
            k = k if arr[0] < k else k + 1 if arr[0] == k else arr[0]
        print("Case {}: {}".format(tc + 1, k))