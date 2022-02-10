"""
106 Miles To Chicago
Source: URI Online Judge   Time Limit: 5000ms   Memory Limit: 512MB
"""

def bellmanford(s, n, edges):
    dist = [0] * (n + 1)
    dist[s] = 100
    index = 0
    while index < n:
        is_update = False
        for u,v,p in edges:
            if dist[u] > 0 and dist[v] < dist[u] * p / 100:
                dist[v] = dist[u] * p / 100
                is_update = True
        if not is_update:
            break
        index += 1
    return dist[n]


def process(n, m):
    edges = []
    for _ in range(m):
        a,b,p = map(int, input().split())
        edges.append((a, b, p))
        edges.append((b, a, p))
    res = bellmanford(1, n, edges)
    print("{:.6f} percent".format(res))


if __name__ == "__main__":
    while True:
        params = input().split()
        if len(params) == 1:
            exit(0)
        n, m = map(int, params)
        process(n, m)