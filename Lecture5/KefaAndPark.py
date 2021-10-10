class KefaPark:
    """
    pack consisting N vertices, root is vertex 1.
    left vertices is restaurant
    cannot go to restaurant when meet M cat consecutive.
    count number restaurant
    INPUT:
    N,M N (1, 10^5), M <= N
    N integer: vertices is has cat.
    N-1 line edge
    OUTPUT:
    number restaurant
    """
    def __init__(self,n,m,cats,edge):
        self.n = n
        self.m = m
        self.cats = cats
        self.edge = edge

    def process(self):
        graph = [[] for i in range(self.n)]

        for e in self.edge:
            graph[e[0]-1].append(e[1]-1)
            graph[e[1]-1].append(e[0]-1)

        queue = []
        visited = [False] * self.n
        queue.append((0, 0))
        visited[0] = True
        count_restaurant = 0

        while len(queue) > 0:
            u_c = queue.pop(0)
            u = u_c[0]
            c = u_c[1]
            if cats[u] == 1:
                c += 1
            else:
                c = 0
            if c > self.m:
                continue

            if len(graph[u]) == 1 and u != 0:
                count_restaurant += 1

            for v in graph[u]:
                if visited[v] is False:
                    visited[v] = True
                    queue.append((v,c))
        return count_restaurant


if __name__ == "__main__":
    n,m = [int(i) for i in input().split()]
    cats =[int(i) for i in input().split()]
    edges = []
    for i in range(n-1):
        edges.append([int(i) for i in input().split()])

    kefaObj = KefaPark(n,m,cats,edges)
    res = kefaObj.process()
    print(res)

