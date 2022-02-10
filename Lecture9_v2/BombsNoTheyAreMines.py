"""
Bombs! NO they are Mines!!
Source: UVA   Time Limit: 3000ms   Memory Limit: 512MB
"""


def bfs(s, e, n, graph):
    visited = [False] * n
    visited[s] = True
    queue = [(0, s)]
    while len(queue) > 0:
        w, u = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                if v == e:
                    return w + 1
                visited[v] = True
                queue.append((w + 1, v))
    return -1


def process(n, m):
    k = int(input())
    matrix = [[0] * m for _ in range(n)]
    for _ in range(k):
        i, c, *arr = list(map(int, input().split()))
        for j in arr:
            matrix[i][j] = 1

    graph = [[] for _ in range(n*m)]
    ar_padding = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                index = i * m + j
                for k, l in ar_padding:
                    ii, jj = i + k, j + l
                    if 0 <= ii < n and 0 <= jj < m and matrix[ii][jj] == 0:
                        graph[index].append(ii * m + jj)
    res = bfs(start[0] * m + start[1], end[0] * m + end[1], n * m, graph)
    print(res)


if __name__ == "__main__":
    while True:
        n,m = map(int, input().split())
        if n == m == 0:
            exit(0)
        process(n,m)

