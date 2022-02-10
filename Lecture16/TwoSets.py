"""
Two Sets
Source: Codeforces   Time Limit: 1000ms   Memory Limit: 256MB
"""


def findSet(u, parents):
    if parents[u] != u:
        parents[u] = findSet(parents[u], parents)
    return parents[u]


def union(u, v, parents, ranks):
    up, vp = findSet(u, parents), findSet(v, parents)
    if up == vp:
        return
    if ranks[up] > ranks[vp]:
        parents[vp] = up
    elif ranks[up] < ranks[vp]:
        parents[up] = vp
    else:
        parents[up] = vp
        ranks[vp] += 1


if __name__ == "__main__":
    n, a, b = map(int, input().split())
    arr = [int(i) for i in input().split()]
    maxArr = max(arr)
    if maxArr >= a and maxArr >= b:
        print("NO")
        exit(0)

    mapArr = {arr[i]: i for i in range(n)}
    parents = [i for i in range(n + 2)]
    ranks = [0] * (n + 2)
    for i in range(1, n + 1):
        u = arr[i-1]

        inA = a - u > 0 and (a - u) in mapArr
        inB = b - u > 0 and (b - u) in mapArr

        if inA:
            offsetA = mapArr[a-u] + 1
            union(i, offsetA, parents, ranks)
        if not inB:
            union(i, n+1, parents, ranks)
        if inB:
            offsetB = mapArr[b - u] + 1
            union(i, offsetB, parents, ranks)
        if not inA:
            union(i, 0, parents, ranks)

    res = [0] * n
    findA = findSet(0, parents)
    findB = findSet(n+1, parents)
    if findA == findB:
        print("NO")
        exit(0)
    for i in range(1, n + 1):
        if findSet(i, parents) == findA:
            res[i-1] = 1

    print("YES")
    print(" ".join(map(str, res)))
