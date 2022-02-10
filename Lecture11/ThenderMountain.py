"""
Thunder Mountain
Source: UVA   Time Limit: 3000ms   Memory Limit: 512MB
"""
INF = 10 ** 10

def floyd(n, dist):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


if __name__ == "__main__":
    nTC = int(input())
    for itc in range(nTC):
        n = int(input())
        dist = [[INF] * n for __ in range(n)]
        points = []
        for __ in range(n):
            x,y = map(int, input().split())
            points.append((x,y))
        for i in range(n):
            for j in range(i, n):
                distance = ((points[i][0] - points[j][0])** 2 + (points[i][1] - points[j][1])** 2) ** 0.5
                if distance <= 10:
                    dist[i][j] = dist[j][i] = distance

        floyd(n, dist)
        maxDistance = 0
        for i in range(n):
            maxDistance = max(maxDistance, max(dist[i]))
        if itc > 0:
            print()
        print("Case #{}:".format(itc + 1))
        if maxDistance == INF:
            print("Send Kurdy")
        else:
            print("{:.4f}".format(maxDistance))
        itc += 1