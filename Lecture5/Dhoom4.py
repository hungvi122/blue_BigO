"""
Dhoom4
Source: HackerEarth   Time Limit: 1000ms   Memory Limit: 512MB
"""

if __name__ == "__main__":
    hKey, bKey = map(int, input().split())
    n = input()
    arr = list(map(int, input().split()))
    visited = [False] * 100000
    queue = [(hKey, 0)]
    if hKey == bKey:
        print(0)
        exit(0)
    while len(queue) > 0:
        u,w = queue.pop(0)
        for t in arr:
            v = u * t % 100000
            if not visited[v]:
                queue.append((v, w + 1))
                visited[v] = True
                if v == bKey:
                    print(w + 1)
                    exit(0)
    print(-1)
