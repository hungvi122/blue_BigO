"""
Validate the Maze
Source: Spoj   Time Limit: 1000ms   Memory Limit: 512MB
"""


def bfs(s, e, n, graph):
    visited = [False] * n
    queue = [s]
    visited[s] = True
    while len(queue) > 0:
        u = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                if v == e:
                    return True
    return False


def checkMaze():
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    arr_entry = []
    ar_padding = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    graph = [[] for _ in range(n * m)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.':
                index = i*m + j
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    arr_entry.append(index)
                for k,l in ar_padding:
                    ii, jj = i + k, j + l
                    if 0 <= ii < n and 0 <= jj < m and matrix[ii][jj] == '.':
                        graph[index].append(ii*m + jj)

    if len(arr_entry) != 2:
        return False
    return bfs(arr_entry[0], arr_entry[1], n*m, graph)


if __name__ == "__main__":
    i_tc = int(input())
    for _ in range(i_tc):
        res = checkMaze()
        if res:
            print("valid")
        else:
            print("invalid")