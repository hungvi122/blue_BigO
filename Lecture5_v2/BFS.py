"""
Breadth First Search: Shortest Reach
Source: HackerRank   Time Limit: 1000ms   Memory Limit: 512MB
"""


def bfs(s, n, dist, graph):
    visited = [False] * (n + 1)
    visited[s] = True
    dist[s] = 0
    queue = [(s, 0)]
    while len(queue) > 0:
        u, w = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                dist[v] = w + 6
                visited[v] = True
                queue.append((v, dist[v]))


if __name__ == "__main__":
    i_tc = int(input())
    for _ in range(i_tc):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n + 1)]
        dist = [-1] * (n + 1)

        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        s = int(input())
        bfs(s, n, dist, graph)
        dist.pop(s)
        print(" ".join(map(str, dist[1:])))