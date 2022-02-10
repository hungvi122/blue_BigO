"""
Sending Email
Source: Uva   Time Limit: 3000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 9


def dijkstra(s, t, n, graph):
    visited = [False] * n
    dist = [INF] * n
    dist[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        visited[u] = True
        if u == t:
            break
        for v,c in graph[u]:
            if not visited[v] and dist[v] > w + c:
                dist[v] = w + c
                pq.put((dist[v], v))
    return dist[t]


def process():
    n,m,s,t = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u,v,w = map(int, input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))
    return dijkstra(s,t,n,graph)


if __name__ == "__main__":
    q = int(input())
    for i in range(1, q + 1):
        res = process()
        print("Case #{}: {}".format(i, res if res != INF else "unreachable"))