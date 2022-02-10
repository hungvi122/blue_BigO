"""
ACM Contest and Blackout
Source: UVA   Time Limit: 1000ms   Memory Limit: 512MB
"""

from queue import PriorityQueue
INF = 10 ** 10


def prim(s, n, graph):
    dist = [INF] * n
    path = [-1] * n
    visited = [False] * n
    pq = PriorityQueue()
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
    return sum(dist[1:]), edges


def process(n, m):
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    value1, edges = prim(1, n + 1, graph)
    value2 = INF
    for u,v,w in edges:
        graph[u].remove((v, w))
        graph[v].remove((u, w))
        cost2, edges2 = prim(1, n + 1, graph)
        value2 = min(value2, cost2)
        if value2 == value1:
            break
        graph[u].append((v, w))
        graph[v].append((u, w))
    print(value1, value2)


if __name__ == "__main__":
    itc = int(input())
    for _ in range(itc):
        n,m = map(int, input().split())
        process(n,m)
        itc += 1