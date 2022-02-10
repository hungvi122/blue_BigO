"""
War
Source: UVa   Time Limit: 2000ms   Memory Limit: 512MB
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


def checkEnemy(u, v, parents):
    if findSet(u, parents) == findSet(v + n, parents):
        return True
    return False


def checkFriend(u, v, parents):
    if findSet(u, parents) == findSet(v, parents):
        return True
    return False


if __name__ == "__main__":
    n = int(input())
    parents = [i for i in range(2*n)]
    ranks = [0] * 2*n
    while True:
        c,x,y = map(int, input().split())
        if c == 0:
            break
        if c == 1:
            if checkEnemy(x, y, parents):
                print(-1)
            else:
                union(x, y, parents, ranks)
                union(x + n, y + n, parents, ranks)
        elif c == 2:
            if checkFriend(x, y, parents):
                print(-1)
            else:
                union(x, y + n, parents, ranks)
                union(x + n, y, parents, ranks)
        elif c == 3:
            if checkFriend(x, y, parents):
                print(1)
            else:
                print(0)
        elif c == 4:
            if checkEnemy(x, y, parents):
                print(1)
            else:
                print(0)
