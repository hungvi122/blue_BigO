"""
Extended traffic
Source: LightOJ   Time Limit: 4000ms   Memory Limit: 512MB
"""
INF = 10 ** 10
def bellmanford(s, n, edges):
    dist = [INF] * n
    dist[s] = 0
    index = 0
    while index < 2 * n:
        is_update = False
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                if index >= n:
                    dist[v] = -INF
                    is_update = True
                else:
                    dist[v] = dist[u] + w
                    is_update = True
        if not is_update:
            break
        index += 1
    return dist


def process(itc):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    m = int(input())
    edges, queries =[], []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v, (arr[v] - arr[u]) ** 3))
    q = int(input())
    for _ in range(q):
        queries.append(int(input()))

    dist = bellmanford(1, n + 1, edges)
    print("Case {}:".format(itc + 1))
    for v in queries:
        if dist[v] < 3 or dist[v] == INF:
            print("?")
        else:
            print(dist[v])


if __name__ == "__main__":
    iTC = int(input())
    for i in range(iTC):
        input()
        process(i)