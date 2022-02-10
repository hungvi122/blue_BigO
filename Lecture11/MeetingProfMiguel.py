"""
Meeting Prof. Miguel ...
Source: UVA   Time Limit: 5000ms   Memory Limit: 512MB
"""
from queue import PriorityQueue
INF = 10 ** 10
SIZE = 26


def dijkstra(s, n, graph):
    visited = [False] * n
    dist = [INF] * n
    dist[s], visited[s] = 0, True
    pq = PriorityQueue()
    pq.put((0,s))
    while len(pq.queue) > 0:
        w, u = pq.get()
        visited[u] = True
        for v, c in graph[u]:
            if not visited[v] and dist[v] > w + c:
                dist[v] = w + c
                pq.put((dist[v], v))
    return dist


def bellmanford(s, n, edges):
    dist = [INF] * n
    dist[s],index = 0, 0
    while index < n:
        is_update = False
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                is_update = True
        if not is_update:
            break
        index += 1
    return dist


def floyd(s, n, dist):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if i == j:
                    continue
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


def processFloyd(n):
    distU = [[INF] * SIZE for _ in range(SIZE)]
    distO = [[INF] * SIZE for _ in range(SIZE)]
    for i in range(SIZE):
        distU[i][i] = distO[i][i] = 0
    for _ in range(n):
        old, direct, A, B, C = input().split()
        u,v,w = ord(A) - ord('A'), ord(B) - ord('A'), int(C)
        if old == 'Y':
            distU[u][v] = min(distU[u][v], w)
            if direct == 'B':
                distU[v][u] = min(distU[v][u], w)
        else:
            distO[u][v] = min(distO[u][v], w)
            if direct == 'B':
                distO[v][u] = min(distO[v][u], w)
    S, E = input().split()
    s, e = ord(S) - ord('A'), ord(E) - ord('A')
    distU[s][s] = distO[e][e] = 0
    floyd(s, SIZE, distU)
    floyd(e, SIZE, distO)
    position, longRoad = 0, INF
    for i in range(SIZE):
        if distU[s][i] != INF and distO[e][i] != INF:
            value = distU[s][i] + distO[e][i]
            if longRoad > value:
                position, longRoad = [chr(ord('A') + i)], value
            elif longRoad == value:
                position.append(chr(ord('A') + i))
    if longRoad == INF:
        print("You will never meet.")
    else:
        print(longRoad, " ".join(position))


def processDijkstra(n):
    graphU = [[] for _ in range(SIZE)]
    graphO = [[] for _ in range(SIZE)]

    for _ in range(n):
        old, direct, A, B, C = input().split()
        u, v, w = ord(A) - ord('A'), ord(B) - ord('A'), int(C)
        if old == 'Y':
            graphU[u].append((v, w))
            if direct == 'B':
                graphU[v].append((u, w))
        else:
            graphO[u].append((v, w))
            if direct == 'B':
                graphO[v].append((u, w))
    S, E = input().split()
    s, e = ord(S) - ord('A'), ord(E) - ord('A')
    distU = dijkstra(s, SIZE, graphU)
    distO = dijkstra(e, SIZE, graphO)

    position, longRoad = 0, INF
    for i in range(SIZE):
        if distU[i] != INF and distO[i] != INF:
            value = distU[i] + distO[i]
            if longRoad > value:
                position, longRoad = [chr(ord('A') + i)], value
            elif longRoad == value:
                position.append(chr(ord('A') + i))
    if longRoad == INF:
        print("You will never meet.")
    else:
        print(longRoad, " ".join(position))


def processBellmanFord(n):
    edgesU, edgesO = [], []
    for _ in range(n):
        old, direct, A, B, C = input().split()
        u, v, w = ord(A) - ord('A'), ord(B) - ord('A'), int(C)
        if old == 'Y':
            edgesU.append((u, v, w))
            if direct == 'B':
                edgesU.append((v, u, w))
        else:
            edgesO.append((u, v, w))
            if direct == 'B':
                edgesO.append((v, u, w))
    S, E = input().split()
    s, e = ord(S) - ord('A'), ord(E) - ord('A')
    distU = bellmanford(s, SIZE, edgesU)
    distO = bellmanford(e, SIZE, edgesO)

    position, longRoad = 0, INF
    for i in range(SIZE):
        if distU[i] != INF and distO[i] != INF:
            value = distU[i] + distO[i]
            if longRoad > value:
                position, longRoad = [chr(ord('A') + i)], value
            elif longRoad == value:
                position.append(chr(ord('A') + i))
    if longRoad == INF:
        print("You will never meet.")
    else:
        print(longRoad, " ".join(position))


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            exit(0)
        # processDijkstra(n)
        # processBellmanFord(n)
        processFloyd(n)

