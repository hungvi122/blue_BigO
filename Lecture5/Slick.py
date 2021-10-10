class Slick:
    """
    count slick and Size
    Input: N, M
    matrix info
    Output:
    number slicks
    lickSize sort and numberSize
    """
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix

    def process(self):
        queue = []
        visited = [False] * self.m * self.n

        graph = [[] for i in range(self.m * self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j] == 1:
                    if i-1 >= 0 and self.matrix[i-1][j] == 1:
                        graph[i*self.m + j].append((i-1)*self.m + j)
                    if i+1 < self.n and self.matrix[i+1][j] == 1:
                        graph[i*self.m + j].append((i+1)*self.m + j)
                    if j-1 >= 0 and self.matrix[i][j-1] == 1:
                        graph[i*self.m + j].append(i*self.m + j - 1)
                    if j+1 < self.m and self.matrix[i][j+1] == 1:
                        graph[i*self.m + j].append(i*self.m + j + 1)

        map_res = {}
        while True:
            i = 0
            while i < self.m * self.n:
                if visited[i] is False and self.matrix[i//self.m][i%self.m] == 1:
                    break
                i += 1
            if i == self.m * self.n:
                break
            count = 0
            queue.append(i)
            visited[i] = True
            while len(queue) > 0:
                count += 1
                u = queue.pop(0)
                if len(graph[u]) > 0:
                    for v in graph[u]:
                        if visited[v] is False:
                            visited[v] = True
                            queue.append(v)

            map_res[count] = map_res.get(count, 0) + 1

        print(sum(map_res.values()))
        keys = sorted(list(map_res.keys()))
        for i in keys:
            print(i, map_res[i])


if __name__ == "__main__":
    while True:
        n,m = [int(i) for i in input().split()]
        if n == 0 and m == 0:
            break
        matrix = []
        for i in range(n):
            matrix.append([int(j) for j in input().split()])

        obj = Slick(n,m,matrix)
        obj.process()