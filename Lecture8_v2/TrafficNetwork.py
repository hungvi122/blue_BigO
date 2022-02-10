"""
Traffic network
Source: Spoj   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue

INF = 10 ** 9
def dijkstra(s, n, dist, graph):
    dist[s] = 0
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        visited[u] = True
        for v, c in graph[u]:
            if not visited[v] and dist[v] > w + c:
                dist[v] = w + c
                pq.put((dist[v],v))


def process():
    n,m,k,s,t = map(int, input().split())

    graph_s = [[] for _ in range(n + 1)]
    graph_t = [[] for _ in range(n + 1)]
    dist_s = [INF] * (n + 1)
    dist_t = [INF] * (n + 1)
    for _ in range(m):
        d,c,l = map(int, input().split())
        graph_s[d].append((c, l))
        graph_t[c].append((d, l))

    dijkstra(s, n + 1, dist_s, graph_s)
    dijkstra(t, n + 1, dist_t, graph_t)

    minDistance, edge = dist_s[t], (0,0)
    for _ in range(k):
        a, b, c = map(int, input().split())
        if dist_s[a] != INF and dist_t[b] != INF and minDistance > dist_s[a] + dist_t[b] + c:
            minDistance, edge = dist_s[a] + dist_t[b] + c, (a,b)
        if dist_s[b] != INF and dist_t[a] != INF and minDistance > dist_s[b] + dist_t[a] + c:
            minDistance, edge = dist_s[b] + dist_t[a] + c, (a, b)

    if minDistance == INF:
        print(-1)
    else:
        print(minDistance)


if __name__ == "__main__":
    iTc = int(input())
    for _ in range(iTc):
        process()