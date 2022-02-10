"""
Connect Campus
Source: UVA   Time Limit: 3000ms   Memory Limit: 512MB
"""
from heapq import heappush, heappop


def prim(s, n, graph):
    visited = [False] * n
    queue = [(0, s)]
    cost = 0
    while len(queue) > 0:
        w, u = heappop(queue)
        if visited[u]:
            continue
        visited[u] = True
        cost += w
        for v,c in graph[u]:
            if not visited[v]:
                heappush(queue, (c, v))
    return cost


def getDistance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def process(n):
    graph = [[] for _ in range(n + 1)]
    points = [tuple(map(int, input().split())) for _ in range(n)]
    points.insert(0, ())
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            distance = getDistance(points[i], points[j])
            graph[i].append((j, distance))
            graph[j].append((i, distance))

    m = int(input())
    for _ in range(m):
        i,j = map(int,input().split())
        graph[i].append((j, 0))
        graph[j].append((i, 0))
    res = prim(1, n+1, graph)
    print("{:.2f}".format(res))


if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            process(n)
        except EOFError:
            exit(0)