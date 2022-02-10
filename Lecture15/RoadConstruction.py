"""
RoadConstruction
Source: LIGHTOJ   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 10


def prim(s, n, graph):
    dist = [INF] * n
    dist[s] = 0
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
                pq.put((c,v))
    return sum(dist)


if __name__ == "__main__":
    iTC = int(input())
    for i in range(iTC):
        input()
        m = int(input())
        graph = [[] for _ in range(m + 1)]
        roads, names = [], []
        for _ in range(m):
            u,v,w = input().split()
            if u not in names:
                names.append(u)
            if v not in names:
                names.append(v)
            iu, iv = names.index(u),  names.index(v)
            roads.append((iu, iv, int(w)))
        n = len(names)
        graph = [[] for _ in range(n)]
        for u,v,w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        res = prim(0, n, graph)
        print("Case {}: {}".format(i + 1, res if res < INF else "Impossible"))
