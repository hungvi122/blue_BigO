""""
Guilty Prince
Source: LightOJ   Time Limit: 1000ms   Memory Limit: 512MB
"""


def bfs(s, n, graph):
    visited = [False] * n
    queue = [s]
    visited[s] = True
    count = 1

    while len(queue) > 0:
        u = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                count += 1
    return count


def checkIland():
    m, n = map(int, input().split())
    matrix = [input() for _ in range(n)]
    ar_padding = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    graph = [[] for _ in range(n * m)]
    start = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.' or matrix[i][j] == '@':
                index = i*m + j
                if matrix[i][j] == '@':
                    start = index
                for k,l in ar_padding:
                    ii, jj = i + k, j + l
                    if 0 <= ii < n and 0 <= jj < m and (matrix[ii][jj] == '.' or matrix[ii][jj] == '@'):
                        graph[index].append(ii*m + jj)

    return bfs(start, n*m, graph)


if __name__ == "__main__":
    i_tc = int(input())
    for i in range(1, i_tc + 1):
        res = checkIland()
        print("Case {}: {}".format(i, res))
