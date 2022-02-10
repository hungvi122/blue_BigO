"""
The last shot
Source: SPOJ   Time Limit: 4000ms   Memory Limit: 512MB
"""



def dfs(i, n, visited, graph):
    visitedd = [False] * n
    visited[i] = visitedd[i] = True
    count = 1
    stack = [i]
    while len(stack) > 0:
        u = stack.pop()
        for v in graph[u]:
            if not visitedd[v]:
                visited[v] = visitedd[v] = True
                stack.append(v)
                count += 1
    return count


if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)

    visited = [False] * (n + 1)
    maxsize = 0
    for i in range(1, n + 1):
        if not visited[i]:
            size = dfs(i, n + 1, visited, graph)
            maxsize = max(maxsize, size)
    print(maxsize)