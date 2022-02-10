"""
Mice and Maze
Source: Spoj   Time Limit: 1000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 10


def dijkstra(s, n, e, t, graph):
    visited = [False] * n
    dist = [INF] * n
    visited[s] = True
    dist[s] = 0
    pq = PriorityQueue()
    pq.put((0, s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        visited[u] = True
        if u == e:
            return True
        for v, c in graph[u]:
            if not visited[v] and dist[v] > c + w and c + w <= t:
                dist[v] = c + w
                pq.put((dist[v], v))
    return False


if __name__ == "__main__":
    n,e,t,m = [int(input()) for _ in range(4)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b,c))
    count = 0
    for i in range(1, n + 1):
        res = dijkstra(i, n + 1, e, t, graph)
        if res:
            count += 1
    print(count)
