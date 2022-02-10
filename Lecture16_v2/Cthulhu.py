"""
Cthulhu
Source: Codeforces   Time Limit: 2000ms   Memory Limit: 256MB
"""

class Info:
    def __init__(self, vertex, edge):
        self.v = vertex
        self.e = edge


def findParent(u, parents):
    if u != parents[u]:
        parents[u] = findParent(parents[u], parents)
    return parents[u]


def union(u, v, parents, ranks, infos):
    up, vp = findParent(u, parents), findParent(v, parents)

    if up == vp:
        infos[up].e += 1
        return
    if ranks[up] > ranks[vp]:
        parents[vp] = up
        infos[up].v += infos[vp].v
        infos[up].e += infos[vp].e + 1
    elif ranks[up] < ranks[vp]:
        parents[up] = vp
        infos[vp].v += infos[up].v
        infos[vp].e += infos[up].e + 1
    else:
        parents[up] = vp
        infos[vp].v += infos[up].v
        infos[vp].e += infos[up].e + 1
        ranks[vp] += 1

def makeSet(n):
    parents = []
    ranks = []
    infos = []
    for i in range(n):
        parents.append(i)
        ranks.append(0)
        infos.append(Info(1,0))
    return parents, ranks, infos


if __name__ == "__main__":
    n,m = map(int, input().split())
    if n < 3:
        print("NO")
        exit(0)
    parents, ranks, infos = makeSet(n+1)
    for i in range(m):
        u,v = map(int, input().split())
        union(u, v, parents, ranks, infos)
    isCthulhu = False
    for info in infos:
        if info.e == info.v == n:
            isCthulhu = True

    if isCthulhu:
        print("FHTAGN!")
    else:
        print("NO")
