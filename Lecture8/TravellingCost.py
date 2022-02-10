"""
Travelling Cost
Source: Spoj   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 9


def dijkstra(s, n, graph):
    visited = [False] * n
    dist = [INF] * n
    visited[s] = True
    dist[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        visited[u] = True
        for v, c in graph[u]:
            if not visited[v] and dist[v] > c + w:
                dist[v] = c + w
                pq.put((dist[v], v))
    return dist


if __name__ == "__main__":
    n = int(input())
    graph = [[] for i in range(501)]
    arr_vertices = []
    for _ in range(n):
        u,v,w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    s = int(input())
    q = int(input())
    arr = [int(input()) for _ in range(q)]
    dist = dijkstra(s, 501, graph)
    for i in arr:
        if dist[i] == INF:
            print("NO PATH")
        else:
            print(dist[i])