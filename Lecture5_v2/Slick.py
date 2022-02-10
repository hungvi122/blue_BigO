"""
Slick
Source: Spoj   Time Limit: 5000ms   Memory Limit: 512MB
"""


def bfs(s, n, visited, graph):
    queue = [s]
    visited[s] = True
    size = 1
    while len(queue) > 0:
        u = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                size += 1
                visited[v] = True
                queue.append(v)
    return size


def processSlick(n, m):
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    mapCount = {}
    countTotal = 0
    graph = [[] for _ in range(n*m)]
    visited = [False] * (m * n)
    ar_padding = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                index = i*m + j
                for k,l in ar_padding:
                    ii, jj = i + k, j + l
                    if 0 <= ii < n and 0 <= jj < m and matrix[ii][jj] == 1:
                        graph[index].append(ii*m + jj)

    for i in range(n*m):
        if matrix[i//m][i%m] == 1 and not visited[i]:
            size = bfs(i, n*m,visited, graph)
            count =mapCount.get(size, 0)
            mapCount[size] = count + 1
            countTotal += 1

    size_key_sort = list(mapCount.keys())
    size_key_sort.sort()

    print(countTotal)
    for key in size_key_sort:
        print("{} {}".format(key, mapCount[key]))


if __name__ == "__main__":
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            exit(0)
        processSlick(n,m)