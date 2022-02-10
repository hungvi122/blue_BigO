"""
ABC Path
Source: SPOJ   Time Limit: 1000ms   Memory Limit: 512MB
"""


def dfs(i, n, graph):
    visited = [False] * n
    visited[i] = True
    count = 1
    stack = [(i, 1)]
    while len(stack) > 0:
        u, w = stack.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append((v, w + 1))
                count = max(count, w + 1)
    return count

def process(iTC, n, m):
    matrix = []
    for _ in range(n):
        matrix.append(input())
    graph = [[] for _ in range(n*m)]
    ar_padding = [(-1, -1), (-1, 0), (-1, 1), (1, 0), (1, 1), (1, -1), (0, -1), (0, 1)]

    start = []
    for i in range(n):
        for j in range(m):
            s = ord(matrix[i][j])
            index = i * m + j
            if s == ord('A'):
                start.append(index)
            for k, l in ar_padding:
                ii, jj = i + k, j + l
                if 0 <= ii < n and 0 <= jj < m and (ord(matrix[ii][jj]) == s + 1):
                    graph[index].append(ii * m + jj)

    size = 0
    for i in start:
        c = dfs(i, n*m, graph)
        size = max(size, c)
    print("Case {}: {}".format(iTC, size))


if __name__ == "__main__":
    i_tc = 1
    while True:
        n,m = map(int, input().split())
        if n == m == 0:
            exit(0)
        process(i_tc, n, m)
        i_tc += 1

