"""
Lakes in Berland
Source: Codeforces   Time Limit: 1000ms   Memory Limit: 512MB
"""

def bfs(s, n, m, visited, graph):
    queue = [s]
    visited[s] = True
    count, arr = 1, [s]
    insector = True
    while len(queue) > 0:
        u = queue.pop(0)
        if u//m == 0 or u //m == n-1 or u%m == 0 or u%m == m-1:
            insector = False
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                arr.append(v)
                count += 1

    if not insector:
        return 0, []
    return count, arr


def replace(s, index, text):
    s = s[0:index] + text + s[index + 1:]
    return s


if __name__ == "__main__":
    n,m,z = map(int, input().split())
    graph = [[] for _ in range(n*m)]
    matrix = []
    for _ in range(n):
        matrix.append(input())
    ar_padding = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '.':
                index = i * m + j
                for k, l in ar_padding:
                    ii, jj = i + k, j + l
                    if 0 <= ii < n and 0 <= jj < m and matrix[ii][jj] == '.':
                        graph[index].append(ii * m + jj)

    visited = [False] * (n * m)
    arrLake = []
    for i in range(n*m):
        if matrix[i//m][i%m] == '.' and not visited[i]:
            size, arr = bfs(i, n, m, visited, graph)
            if size > 0:
                arrLake.append((size,arr))

    arrLake.sort()
    arrUpdate = []
    for i in range(len(arrLake) - z):
        arrUpdate.extend(arrLake[i][1])
    for index in arrUpdate:
        i, j = index//m, index%m
        matrix[i] = replace(matrix[i], j, '*')

    print(len(arrUpdate))
    for i in range(n):
        print(matrix[i])