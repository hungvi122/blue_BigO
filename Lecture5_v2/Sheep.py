"""
Sheep
Nguồn bài: SPOJ   Giới hạn thời gian: 1000ms   Giới hạn bộ nhớ: 512MB
"""


def bfs(s, n, m, matrix, visited, graph):
    queue = [s]
    visited[s] = True
    countSheep, countWorf = 0, 0
    insector = True
    while len(queue) > 0:
        u = queue.pop(0)
        if u//m == 0 or u //m == n-1 or u%m == 0 or u%m == m-1:
            insector = False
        if matrix[u // m][u % m] == 'k':
            countSheep += 1
        if matrix[u // m][u % m] == 'v':
            countWorf += 1
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    if not insector:
        return 0,0
    if countSheep > countWorf:
        return 0, countWorf
    return countSheep, 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(input())
    ar_padding = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    graph = [[] for _ in range(n * m)]
    visited = [False] * (n * m)
    totalWorf, totalSheep = 0, 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != '#':
                index = i * m + j
                if matrix[i][j] == 'k':
                    totalSheep += 1
                elif matrix[i][j] == 'v':
                    totalWorf += 1
                for k, l in ar_padding:
                    ii, jj = i + k, j + l
                    if 0 <= ii < n and 0 <= jj < m and matrix[ii][jj] != '#':
                        graph[index].append(ii * m + jj)

    for i in range(n*m):
        if matrix[i//m][i%m] != '#' and not visited[i]:
            result = bfs(i, n, m, matrix, visited, graph)
            totalSheep -= result[0]
            totalWorf -= result[1]
    print(totalSheep, totalWorf)
