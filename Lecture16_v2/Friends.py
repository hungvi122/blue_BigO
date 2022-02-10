"""
Friends
Source: UVa   Time Limit: 3000ms   Memory Limit: 512MB
"""


def findSet(u, parents):
    if parents[u] != u:
        parents[u] = findSet(parents[u], parents)
    return parents[u]


def union(u, v, parents, ranks, countArrs):
    up, vp = findSet(u, parents), findSet(v, parents)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parents[vp] = up
        countArrs[up] += countArrs[vp]
    elif ranks[up] < ranks[vp]:
        parents[up] = vp
        countArrs[vp] += countArrs[up]
    else:
        parents[up] = vp
        countArrs[vp] += countArrs[up]
        ranks[vp] += 1


def makeSet(n):
    parents = [i for i in range(n)]
    ranks = [0] * n
    countArrs = [1] * n
    return parents, ranks, countArrs


if __name__ == "__main__":
    itc = int(input())
    for _ in range(itc):
        n, m = map(int, input().split())
        parents, ranks, countArrs = makeSet(n+1)
        for _ in range(m):
            u, v = map(int, input().split())
            union(u, v, parents, ranks, countArrs)
        print(max(countArrs))
