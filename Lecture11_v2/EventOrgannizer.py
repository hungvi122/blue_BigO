"""
Event Organizer
Source: Codechef   Time Limit: 1000ms   Memory Limit: 256MB
"""
SIZE = 49

def floyd(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i <= k <= j and dist[i][j] < dist[i][k] + dist[k][j] - dist[k][k]:
                    dist[i][j] = dist[i][k] + dist[k][j] - dist[k][k]


if __name__ == "__main__":
    itc = int(input())
    for _ in range(itc):
        n = int(input())
        dist = [[0] * SIZE for ___ in range(SIZE)]
        jobs = []
        for __ in range(n):
            s,e,c = map(int, input().split())
            dist[s][e] = max(dist[s][e], c)
        floyd(SIZE, dist)
        print(dist[0][SIZE-1])