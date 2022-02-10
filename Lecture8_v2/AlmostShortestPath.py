"""
Almost Shortest Path
Source: UVa   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 10


def dijkstra(s, t, n, path, dist, graph):
    visited = [False] * n
    dist[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        visited[u] = True
        if u == t:
            break
        for v, c, i in graph[u]:
            if not visited[v]:
                if dist[v] > w + c:
                    dist[v] = w + c
                    pq.put((dist[v], v))
                    path[v] = [(u, i)]
                elif dist[v] == w + c:
                    path[v].append((u, i))


def process(n, m):
    s, t = map(int, input().split())
    graph = [[] for _ in range(n)]
    dist = [INF] * n
    path = [[] for _ in range(n)]
    edges = []
    removeEdges = [False] * m
    for i in range(m):
        u,v, w = map(int, input().split())
        graph[u].append((v, w, i))
        edges.append((u, v, w))

    dijkstra(s, t, n, path, dist, graph)
    queue = []
    queue.extend(path[t])
    while len(queue) > 0:
        u, i = queue.pop(0)
        removeEdges[i] = True
        queue.extend(path[u])

    graph2 = [[] for _ in range(n)]
    dist2 = [INF] * n
    path2 = [[] for _ in range(n)]
    for i in range(m):
        if not removeEdges[i]:
            u,v,w = edges[i]
            graph2[u].append((v, w, i))

    dijkstra(s, t, n, path2, dist2, graph2)
    if dist2[t] == INF:
        print(-1)
    else:
        print(dist2[t])


if __name__ == "__main__":
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            exit(0)
        process(n, m)