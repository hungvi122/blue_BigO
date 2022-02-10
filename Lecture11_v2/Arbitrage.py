"""
Arbitrage
Source: UVA   Time Limit: 1000ms   Memory Limit: 512MB
"""
INF = 10 ** 10

def floyd(n, dist):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == 0:
                continue
            for j in range(n):
                if dist[k][j] > 0 and dist[i][j] < dist[i][k] * dist[k][j]:
                    dist[i][j] = dist[i][k] * dist[k][j]


def process(itc, n):
    names = [input() for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 1
    m = int(input())
    for _ in range(m):
        a, c, b = input().split()
        u,v,w = names.index(a), names.index(b), float(c)
        dist[u][v] = w

    floyd(n, dist)
    isCycle = False
    for i in range(n):
        if dist[i][i] > 1:
            isCycle = True
    print("Case {}: {}".format(itc, "Yes" if isCycle else "No"))


if __name__ == "__main__":
    itc = 1
    while True:
        n = int(input())
        if n == 0:
            exit(0)
        process(itc, n)
        itc += 1
        input()