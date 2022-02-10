"""
Special subtree
Source: Hackerrank   Time Limit: 2000ms   Memory Limit: 512MB
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
    n,m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u,v,w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    s = int(input())
    res = prim(s, n + 1, graph)
    print(res)
