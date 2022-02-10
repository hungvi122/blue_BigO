"""
Alice in Amsterdam, I mean Wonderland
Source: SPOJ   Time Limit: 4000ms   Memory Limit: 512MB
"""
INF = 10 ** 10
def bellmanford(s, n, edges):
    dist = [INF] * n
    dist[s] = 0
    index = 0
    while index < n:
        is_update = False
        for (u, v, w) in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                is_update = True
        if not is_update:
            break
        index += 1
    if index == n:
        return dist, True
    return dist, False


def process(iTc, n):
    edges = []
    names = []
    for i in range(n):
        params = input().split()
        name = params[0]
        arr = list(map(int, params[1:]))
        names.append(name)
        for j in range(n):
            if arr[j] != 0:
                edges.append((i,j,arr[j]))
    q = int(input())
    graphQueries = [[] for _ in range(n)]
    queries, mapRes = [], dict()
    for _ in range(q):
        u, v = map(int, input().split())
        queries.append((u,v))
        graphQueries[u].append(v)

    for i in range(n):
        if len(graphQueries[i]) > 0:
            dist, cycle = bellmanford(i, n, edges)
            for v in graphQueries[i]:
                mapRes[(i, v)] = (cycle, dist[v])

    print("Case #{}:".format(iTc))
    for u,v in queries:
        cycle, w = mapRes[(u, v)]
        if cycle:
            print("NEGATIVE CYCLE")
        else:
            print("{}-{} {}".format(names[u], names[v], "NOT REACHABLE" if w == INF else w))


if __name__ == "__main__":
    iTC = 1
    while True:
        n = int(input())
        if n == 0:
            exit(0)
        process(iTC, n)
        iTC += 1