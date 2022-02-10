"""
Kefa and Park
Source: Codeforces   Time Limit: 2000ms   Memory Limit: 256MB
"""


def bfs(n, m, arr_cats, graph):
    visited = [False] * (n + 1)
    queue = [(1, arr_cats[1])]
    visited[1] = True
    count = 0
    while len(queue) > 0:
        u, w = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                ww = 0 if arr_cats[v] == 0 else w + 1
                if ww <= m:
                    queue.append((v, ww))
                    if len(graph[v]) == 1:
                        count += 1
                visited[v] = True
    return count


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr_cat = [0]
    for ch in input().split():
        arr_cat.append(int(ch))

    graph = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    res = bfs(n, m, arr_cat, graph)
    print(res)

