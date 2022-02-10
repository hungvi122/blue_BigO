"""
Dudu service maker
Nguồn bài: URIONLINEJUDGE   Giới hạn thời gian: 2000ms   Giới hạn bộ nhớ: 512MB
"""
import sys
sys.setrecursionlimit(10000)


def dfs(u, visited, graph):
    visited[u] = 1
    for v in graph[u]:
        if visited[v] == 0:
            res = dfs(v, visited, graph)
            if res:
                return res
        elif visited[v] == 1:
            return True
    visited[u] = 2
    return False


def process():
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)

    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == 0:
            check = dfs(i, visited, graph)
            if check:
                print("YES")
                return
    print("NO")
    return


if __name__ == "__main__":
    i_tc = int(input())
    for _ in range(i_tc):
        process()