"""
Ice Cave
Source: CodeForces   Time Limit: 1000ms   Memory Limit: 512MB
"""


def bfs(s, e, n, graph):
    visited = [False] * n
    visited[s] = True
    queue = [s]
    while len(queue) > 0:
        u = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                if v == e:
                    return True
                visited[v] = True
                queue.append(v)
    return False


if __name__ == "__main__":
    n,m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(input())
    ar_padding = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    graph = [[] for _ in range(n * m)]
    start = tuple(map(lambda ch: int(ch) - 1, input().split()))
    end = tuple(map(lambda ch: int(ch) - 1, input().split()))
    countIntactEnd = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.' or (i == start[0] and j == start[1]):
                index = i * m + j
                for k, l in ar_padding:
                    ii, jj = i + k, j + l
                    if 0 <= ii < n and 0 <= jj < m and (matrix[ii][jj] == '.' or (ii == end[0] and jj == end[1])):
                        graph[index].append(ii * m + jj)
                        if i == end[0] and j == end[1]:
                            countIntactEnd += 1

    if matrix[end[0]][end[1]] == '.' and countIntactEnd < 2:
        print("NO")
        exit(0)
    i_start = start[0] * m + start[1]
    i_end = end[0] * m + end[1]
    status = bfs(i_start, i_end, n * m, graph)
    if status:
        print("YES")
    else:
        print("NO")
