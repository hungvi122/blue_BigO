"""
Risk
Source: UVA   Time Limit: 1000ms   Memory Limit: 512MB
"""
INF = 10 ** 10
SIZE = 21


def floyd(n, dist):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if i == j:
                    continue
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


def process(itc):
    try:
        dist = [[INF] * SIZE for _ in range(SIZE)]
        for i in range(1, SIZE - 1):
            arr = list(map(int, input().split()))
            dist[i][i] = 0
            for j in arr[1:]:
                dist[i][j] = dist[j][i] = 1
        floyd(SIZE, dist)
        n = int(input())
        if itc > 1:
            print()
        print("Test Set #{}".format(itc))
        for _ in range(n):
            u, v = map(int, input().split())
            print("{} to {}: {}".format(str(u).rjust(2, ' '), str(v).rjust(2, ' '), dist[u][v]))
    except EOFError:
        return False
    return True


if __name__ == "__main__":
    itc = 1
    while True:
        is_continue = process(itc)
        if not is_continue:
            exit(0)
        itc += 1