"""
Asterix and Obelix
Source: UVA   Time Limit: 3000ms   Memory Limit: 512MB
"""
INF = 10 ** 10


def floyd(n, parties, dist):
    is_update = False
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if i == j:
                    continue
                if dist[k][j] != INF and (dist[i][j] == INF or dist[i][j] + parties[i][j] > dist[i][k] + dist[k][j] +
                                          max(parties[i][k], parties[k][j])):
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parties[i][j] = max(parties[i][k], parties[k][j])
                    is_update = True
    return is_update


def process(c, r, q):
    dist = [[INF] * (c+1) for _ in range(c+1)]
    parties = [[0] * (c+1) for _ in range(c+1)]
    arr = [0]
    arr.extend(list(map(int, input().split())))
    for i in range(1,c+1):
        parties[i][i] = arr[i]

    for _ in range(r):
        u, v, w = map(int, input().split())
        dist[u][v] = dist[v][u] = w
        parties[u][v] = parties[v][u] = max(arr[u], arr[v])
    queries = []
    for _ in range(q):
        u,v = map(int, input().split())
        queries.append((u,v))
    is_Continue = True
    while is_Continue:
        is_Continue = floyd(c+1, parties, dist)
    for u,v in queries:
        if dist[u][v] == INF:
            print(-1)
        else:
            print(dist[u][v] + parties[u][v])


if __name__ == "__main__":
    iTC = 1
    while True:
        c, r, q = map(int, input().split())
        if c == r == q == 0:
            exit(0)
        if iTC > 1:
            print()
        print("Case #{}".format(iTC))
        process(c,r,q)
        iTC += 1