"""
Simulator network
Source: Hackerearth   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 10

def prim(s, n, graph):
    dist = [INF] * n
    dist[s] = 0
    path = [-1] * n
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0,s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        if visited[u]:
            continue
        visited[u] = True
        for v, c in graph[u]:
            if not visited[v] and dist[v] > c:
                dist[v] = c
                path[v] = u
                pq.put((c,v))
    return dist[s+1:]


if __name__ == "__main__":
    n,m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u,v,w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    q = int(input())
    caps = list(map(int, input().split()))
    res = prim(1, n + 1, graph)
    res.extend(caps)
    res.sort()
    print(sum(res[0:n-1]))
