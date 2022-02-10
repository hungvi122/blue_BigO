"""
Cobbed streets
Source: SPOJ   Time Limit: 1500ms   Memory Limit: 512MB
"""

from queue import PriorityQueue


def prim(s, n, graph):
    cost = 0
    visited = [False] * (n + 1)
    pq = PriorityQueue()
    pq.put((0,s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        if visited[u]:
            continue
        visited[u] = True
        cost += w
        for v,c in graph[u]:
            if not visited[v]:
                pq.put((c,v))
    return cost


if __name__ == "__main__":
    iTC = int(input())
    for _ in range(iTC):
        p,n,m = [int(input()) for _ in range(3)]
        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            u,v,w = map(int, input().split())
            graph[u].append((v, w))
            graph[v].append((u, w))
        res = prim(1, n + 1, graph)
        print(res*p)
