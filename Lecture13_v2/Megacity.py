"""
Megacity
Source: Codeforces   Time Limit: 2000ms   Memory Limit: 512MB
"""

if __name__ == "__main__":
    n, s = map(int, input().split())
    arr = []
    for i in range(n):
        x, y, w = map(int, input().split())
        distance = (x*x + y*y) ** 0.5
        arr.append((distance, w))
    arr.sort()
    for d, w in arr:
        s += w
        if s >= 10 ** 6:
            print("{:.7f}".format(d))
            exit(0)
    print(-1)

