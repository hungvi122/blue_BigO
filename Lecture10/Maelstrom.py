"""
Maelstrom
Nguồn bài: UVA   Giới hạn thời gian: 3000ms   Giới hạn bộ nhớ: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 8

def dijkstra(s, n, graph):
    visited = [False] * n
    pq = PriorityQueue()
    dist = [INF] * n
    dist[s] = 0
    pq.put((0,s))
    while len(pq.queue) > 0:
        w,u = pq.get()
        visited[u] = True
        for (v, c) in graph[u]:
            if not visited[v] and dist[v] > w + c:
                dist[v] = w + c
                pq.put((dist[v], v))
    return dist


def bellmanford(s, n, edges):
    dist = [INF] * n
    dist[s] = 0
    index = 0
    while index < n:
        is_update = False
        for (u,v,w) in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                is_update = True
        if not is_update:
            break
        index += 1
    return dist


if __name__ == "__main__":
    n = int(input())
    edges = []
    graph = [[] for _ in range(n)]
    for i in range(1, n):
        arr = input().split()
        for j in range(i):
            if arr[j] != 'x':
                w = int(arr[j])
                edges.append((i, j, w))
                edges.append((j, i, w))
                graph[i].append((j, w))
                graph[j].append((i, w))
    dist = bellmanford(0, n, edges)
    # dist = dijkstra(0, n, graph)
    res = max(dist)
    print(res)

