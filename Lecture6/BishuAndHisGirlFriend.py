"""
Bishu and his Girlfriend
Source: HACKEREARTH   Time Limit: 1000ms   Memory Limit: 512MB
"""

def dfs(s, n, arr, graph):
    visited = [False] * n
    stack = [(s, 0)]
    visited[s] = True
    indexMin = [n,n]
    while len(stack) > 0:
        u,w = stack.pop()
        if arr[u]:
            if w < indexMin[1]:
                indexMin = [u,w]
            elif w == indexMin[1]:
                indexMin = [min(indexMin[0], u), w]
        for v in graph[u]:
            if not visited[v]:
                stack.append((v, w + 1))
                visited[v] = True
    return indexMin[0]


if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    m = int(input())
    arr = [False] * (n + 1)
    for _ in range(m):
        index = int(input())
        arr[index] = True

    res = dfs(1, n + 1, arr, graph)
    print(res)