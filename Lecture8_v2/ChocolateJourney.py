"""
Chocolate Journey
Source: Hackerearth   Time Limit: 2000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 10


def dijkstra(s, n, x, dist, graph):
    visited = [False] * n
    dist[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        visited[u] = True
        for v, c in graph[u]:
            if not visited[v] and dist[v] > w + c and w + c <= x:
                dist[v] = w + c
                pq.put((dist[v], v))


if __name__ == "__main__":
    n, m, k, x = map(int, input().split())
    cities = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u,v,w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    a,b = map(int, input().split())

    dist_a = [INF] * (n + 1)
    dist_b = [INF] * (n + 1)
    dijkstra(a, n + 1, INF,  dist_a, graph)
    dijkstra(b, n + 1, x, dist_b, graph)
    minTime = INF
    for city in cities:
        if dist_a[city] != INF and dist_b[city] != INF and dist_b[city] <= x:
            minTime = min(minTime, dist_a[city] + dist_b[city])

    print(minTime if minTime != INF else -1)
