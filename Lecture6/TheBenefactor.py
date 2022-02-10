"""
The Benefactor
Source: SPOJ   Time Limit: 1000ms   Memory Limit: 512MB
"""


def dfs(i, n, dist, graph):
    visited = [False] * n
    visited[i] = True
    stack = [(i, 0)]
    dist[i] = 0
    while len(stack) > 0:
        u, w = stack.pop()
        for v, t in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append((v, w + t))
                dist[v] = w + t

def process():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        u,v,w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    dist = [0] * (n + 1)
    dfs(1, n + 1, dist, graph)
    distMax = max(dist)
    index = dist.index(distMax)
    dist = [0] * (n + 1)
    dfs(index, n + 1, dist, graph)
    print(max(dist))


if __name__ == "__main__":
    itc = int(input())
    for _ in range(itc):
        process()