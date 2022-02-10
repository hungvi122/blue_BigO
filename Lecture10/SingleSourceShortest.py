"""
Single source shortest path, negative weights
Source: Kattis   Time Limit: 5000ms   Memory Limit: 512MB
"""
INF = 10 ** 10


def bellmanford(s, n, edges):
    dist = [INF] * n
    dist[s], index = 0, 0
    while index < 2 * n:
        is_update = False
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                is_update = True
                dist[v] = dist[u] + w if index < n else -INF
        if not is_update:
            break
        index += 1
    return dist


if __name__ == "__main__":
    itc = 0
    while True:
        n,m,q,s = map(int, input().split())
        if n == m == 0:
            exit(0)
        edges = []
        for _ in range(m):
            u,v,w = map(int,input().split())
            edges.append((u,v,w))
        queries = [int(input()) for __ in range(q)]
        dist = bellmanford(s, n, edges)

        if itc != 0:
            print("")
        for v in queries:
            if dist[v] == INF:
                print("Impossible")
            elif dist[v] == -INF:
                print("-Infinity")
            else:
                print(dist[v])
        itc += 1
