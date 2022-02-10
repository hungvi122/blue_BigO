"""
Audiophobia
Source: UVa   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 10


def prim(n, graph):
    dist = [INF] * n
    path = [-1] * n
    visited = [False] * n
    pq = PriorityQueue()
    for s in range(1, n):
        if not visited[s]:
            pq.put((0, s))
            dist[s] = 0
        while len(pq.queue) > 0:
            w, u = pq.get()
            if visited[u]:
                continue
            visited[u] = True
            for v, c in graph[u]:
                if not visited[v] and dist[v] > c:
                    dist[v] = c
                    path[v] = u
                    pq.put((c, v))

    edges = []
    for v in range(1, n):
        if v > 0 and path[v] > 0:
            edges.append((v, path[v], dist[v]))
    return edges


def bfs(s, e, n, graph):

    path = [(-1, INF)] * n
    visited = [False] * n
    queue = [s]
    visited[s] = True
    while len(queue) > 0:
        u = queue.pop(0)
        for v, c in graph[u]:
            if v > 0 and not visited[v]:
                visited[v] = True
                path[v] = (u, c)
                if v == e:
                    break
                queue.append(v)

    maxDist = 0
    if path[e][1] == INF:
        return INF
    while e != -1 and e != s:
        maxDist = max(maxDist, path[e][1])
        e = path[e][0]
    return maxDist


def process(tc, n, m, q):
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    if tc > 1:
        print()
    edges = prim(n + 1, graph)
    graphBFS = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graphBFS[u].append((v, w))
        graphBFS[v].append((u, w))

    print("Case #{}".format(itc))
    for _ in range(q):
        s, e = map(int, input().split())
        res = bfs(s, e, n + 1, graphBFS)
        if res == INF:
            print("no path")
        else:
            print(res)


if __name__ == "__main__":
    itc = 1
    while True:
        c,s,q = map(int, input().split())
        if c == 0:
            exit(0)
        process(itc,c,s,q)
        itc += 1