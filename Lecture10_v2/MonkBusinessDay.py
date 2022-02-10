"""
Monk's Business Day
Source: Hackerearth   Time Limit: 2000ms   Memory Limit: 256MB
"""
INF = 10 ** 10

def bellmanford(s, n, edges):
    dist = [-INF] * (n + 1)
    dist[s], index = 0, 0
    while index < 2 * n:
        is_update = False
        for u, v, w in edges:
            if dist[u] != -INF and dist[v] < dist[u] + w:
                is_update = True
                dist[v] = dist[u] + w if index < n else INF
        if not is_update:
            break
        index += 1
    return index >= n


if __name__ == "__main__":
    itc = int(input())
    for _ in range(itc):
        n, m = map(int, input().split())
        edges = []
        for __ in range(m):
            i, j, c = map(int, input().split())
            edges.append((i,j,c))
        res = bellmanford(1, n, edges)
        print("Yes" if res else "No")