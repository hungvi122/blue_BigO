"""
Possible Friend
Source: SPOJ   Time Limit: 4000ms   Memory Limit: 512MB
"""
INF = 10 ** 10


def floyd(n, dist):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] != INF and dist[i][k] + dist[k][j] <= 2 and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


def process():
    matrix = []
    row = input()
    size = len(row)
    matrix.append(row)
    for i in range(1, size):
        matrix.append(input())

    dist = [[INF] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            dist[i][j] = 0 if i == j else 1 if matrix[i][j] == 'Y' else INF
    floyd(size, dist)
    index, countSize = 0, 0
    for i in range(size):
        count = 0
        for j in range(size):
            if dist[i][j] == 2:
                count += 1
        index, countSize = (i, count) if countSize < count else (index, countSize)

    print(index, countSize)


if __name__ == "__main__":
    iTC = int(input())
    for _ in range(iTC):
        process()