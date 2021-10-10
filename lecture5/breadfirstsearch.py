class DFS:
    """describe:
    undirected graph N node, 1-N. length edge = 6
    start S, to all other retain Node
    Input: number TestCase N
    Number Node, Number Edge
    List Edge
    Output:print Inline order by number Node + num path to Node from S.
    """
    def __init__(self, n, edge, s, w):
        self.n = n
        self.edge = edge
        self.s = s
        self.w = w


    def process(self):
        visited = [False] * (self.n + 1)
        path = [-1] * (self.n + 1)
        graph = [[] for i in range(self.n + 1)]
        for e in self.edge:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        queue = []

        visited[self.s] = True
        queue.append(self.s)

        while len(queue) > 0:
            u = queue.pop(0)
            if len(graph[u]) > 0:
                for v in graph[u]:
                    if visited[v] is False:
                        visited[v] = True
                        path[v] = u
                        queue.append(v)

        # process path.
        path_res = [-1] * (self.n - 1)
        index = 0
        for i in range(1, self.n + 1):
            if i == self.s:
                continue
            path_i = -1
            if path[i] > 0:
                count = 0
                v = i
                while v != self.s:
                    v = path[v]
                    count += 1
                path_i = count * self.w
            path_res[index] = path_i
            index += 1
        return path_res


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        n, edge_size = [int(i) for i in input().split()]
        edge = []
        for i in range(edge_size):
            edge_i = tuple(int(e) for e in input().split())
            edge.append(edge_i)

        s = int(input())
        dfs = DFS(n, edge, s, 6)
        res = dfs.process()
        print(" ".join(map(str, res)))
