"""
Commandos
Source: LightOJ   Time Limit: 500ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 10


def dijkstra(s, n, dist, graph):
    visited = [False] * n
    dist[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        visited[u] = True
        for v in graph[u]:
            if not visited[v] and dist[v] > w + 1:
                dist[v] = w + 1
                pq.put((dist[v], v))


def process():
    n,r = int(input()), int(input())
    graph = [[] for _ in range(n)]
    for _ in range(r):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s, t = map(int, input().split())
    dist_s = [INF] * n
    dist_t = [INF] * n
    dijkstra(s, n, dist_s, graph)
    dijkstra(t, n, dist_t, graph)
    maxTime = -1
    for i in range(n):
        if dist_s[i] != INF and dist_t[s] != INF:
            maxTime = max(dist_s[i] + dist_t[i], maxTime)
    return maxTime


if __name__ == "__main__":
    iTC = int(input())
    for i in range(iTC):
        res = process()
        print("Case {}: {}".format(i + 1, res))
