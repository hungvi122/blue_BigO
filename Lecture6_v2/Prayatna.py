"""
Prayatna
Nguồn bài: SPOJ   Giới hạn thời gian: 1000ms   Giới hạn bộ nhớ: 512MB
"""


def dfs(i, visited, graph):
    stack = [i]
    visited[i] = True
    while len(stack) > 0:
        u = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)


def process():
    n = int(input())
    graph = [[] for _ in range(n)]
    visited = [False] * n
    m = int(input())
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, graph)
            count += 1
    print(count)


if __name__ == "__main__":
    i_tc = int(input())
    for _ in range(i_tc):
        process()
