"""
XYZZY
Source: UVa   Time Limit: 3000ms   Memory Limit: 512MB
"""
INF = 10 ** 10
def bellmanford(s, energy, n, edges):
    dist = [-INF] * (n + 1)
    dist[s], index = energy, 0
    while index < 2 * n:
        is_update = False
        for u, v, w in edges:
            if dist[u] > 0 and dist[u] + w > 0 and dist[v] < dist[u] + w:
                if index < n:
                    dist[v] = dist[u] + w
                else:
                    dist[v] = INF
                is_update = True
        if not is_update:
            break
        index += 1
    return dist[n] > 0


def process(n):
    edges = []
    graph = [[] for _ in range(n + 1)]
    arr_energy = [0] * (n + 1)
    for i in range(1, n + 1):
        w, c, *arr = list(map(int, input().split()))
        arr_energy[i] = w
        for j in arr:
            graph[i].append(j)
    for i in range(n + 1):
        if len(graph[i]) > 0:
            for j in graph[i]:
                edges.append((i, j, arr_energy[j]))

    res = bellmanford(1, 100, n, edges)
    if res:
        print("winnable")
    else:
        print("hopeless")


if __name__ == "__main__":
    while True:
        n = int(input())
        if n < 0:
            exit(0)
        process(n)