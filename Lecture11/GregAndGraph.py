"""
Greg and graph
Source: Codeforces   Time Limit: 1000ms   Memory Limit: 256MB
"""
INF = 10 ** 10


def copydist(distG, dist, v, arrK):
    for i in arrK:
        dist[v][i] = distG[v][i]
        dist[i][v] = distG[i][v]


def floyd(n, arrK, dist):
    for k in arrK:
        for i in arrK:
            if i == k:
                continue
            for j in arrK:
                if i == j:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    sumDist = 0
    for i in range(n):
        for j in range(n):
            sumDist += 0 if dist[i][j] == INF else dist[i][j]
    return sumDist


if __name__ == "__main__":
    n = int(input())
    distG = []
    for i in range(n):
        arr = list(map(int, input().split()))
        distG.append(arr)
    arrDelete = list(map(lambda i: int(i) - 1, input().split()))
    arrDelete.reverse()
    res = []
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        v, arrK = arrDelete[i], arrDelete[:i+1]
        copydist(distG, dist, v, arrK)
        dist[v][v] = 0
        sumDist = floyd(n, arrK, dist)
        res.append(sumDist)
    res.reverse()
    print(" ".join(map(str, res)))
