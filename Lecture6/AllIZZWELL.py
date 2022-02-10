"""
ALL IZZ WELL
Source: SPOJ   Time Limit: 1000ms   Memory Limit: 512MB
"""
text = "ALLIZZWELL"


def dfs(u, w, n, m, visited, matrix, graph):
    visited[u] = True
    if w == len(text) - 1:
        return True
    for v in graph[u]:
        ch = matrix[v//m][v%m]
        if not visited[v] and ch == text[w+1]:
            res = dfs(v, w + 1, n, m, visited, matrix, graph)
            if res:
                return res
    visited[u] = False
    return False


def process(n, m):
    matrix = []
    for _ in range(n):
        matrix.append(input())
    graph = [[] for _ in range(n*m)]
    visited = [False] * (n * m)
    ar_padding = [(-1, -1), (-1, 0), (-1, 1), (1, 0), (1, 1), (1, -1), (0, -1), (0, 1)]

    start = []
    for i in range(n):
        for j in range(m):
            ch = matrix[i][j]
            if ch not in text:
                continue
            index = i * m + j
            if ch == 'A':
                start.append(index)
            for k, l in ar_padding:
                ii, jj = i + k, j + l
                if 0 <= ii < n and 0 <= jj < m and matrix[ii][jj] in text:
                    chh = matrix[ii][jj]
                    if (ch + chh) in text:
                        graph[index].append(ii * m + jj)
    for i in start:
        status = dfs(i, 0, n, m, visited, matrix, graph)
        if status:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    i_tc = int(input())
    for i in range(i_tc):
        n,m = map(int, input().split())
        process(n, m)
        if i < i_tc - 1:
            input()

