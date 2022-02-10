"""
Wormholes
Source: UVa   Time Limit: 3000ms   Memory Limit: 512MB
"""

INF = 10 ** 9
def bellmanford(s, n, edges):
    dist = [INF] * n
    dist[s] = 0
    i = 0
    while i < n:
        is_update = False
        for (u, v, w) in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                is_update = True
        if not is_update:
            break
        i += 1
    if i == n:
        return True
    return False


def process():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u,v,w = map(int, input().split())
        edges.append((u,v,w))
    res = bellmanford(0, n, edges)
    if res:
        print("possible")
    else:
        print("not possible")


if __name__ == "__main__":
    itc = int(input())
    for _ in range(itc):
        process()
