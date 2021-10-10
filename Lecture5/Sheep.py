class CountResult:
    def __init__(self, sheep, wolf, isInSector):
        self.sheep = sheep
        self.wolf = wolf
        self.in_sector = isInSector


class Sheep:
    """
    . is space, # is fence
    backyard is rectangle: n,m
    k is sheep, v is wolf
    INPUT:
    N,M, matrix
    OUTPUT:
    sheep and wolf survive
    """
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix

    def process(self):
        queue = []
        visited = [False] * self.n * self.m
        graph = [[] for i in range(self.n * self.m)]

        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j] != '#':
                    if i - 1 >= 0 and self.matrix[i-1][j] != '#':
                        graph[i*self.m + j].append((i-1) * self.m + j)
                    if i + 1 < self.n and self.matrix[i+1][j] != '#':
                        graph[i*self.m + j].append((i+1) * self.m + j)
                    if j - 1 >= 0 and self.matrix[i][j-1] != '#':
                        graph[i*self.m + j].append(i * self.m + j - 1)
                    if j + 1 < self.m and self.matrix[i][j+1] != '#':
                        graph[i*self.m + j].append(i * self.m + j + 1)

        i = 0
        count_sheep, count_wolf = 0,0
        while True:
            while i < self.m * self.n:
                if visited[i] is False and self.matrix[i//self.m][i%self.m] != '#':
                    break
                i += 1

            if i == self.m * self.n:
                break

            queue.append(i)
            visited[i] = True

            count_item = CountResult(0,0,True)
            while len(queue) > 0:
                u = queue.pop(0)
                if self.matrix[u//self.m][u%self.m] == 'k':
                    count_item.sheep += 1
                if self.matrix[u//self.m][u%self.m] == 'v':
                    count_item.wolf += 1
                if u//self.m == 0 or u//self.m == n-1 or u%self.m == 0 or u%self.m == m-1:
                    count_item.in_sector = False

                if len(graph[u]) == 0:
                    continue
                for v in graph[u]:
                    if visited[v] is False:
                        visited[v] = True
                        queue.append(v)

            if count_item.in_sector:
                if count_item.sheep > count_item.wolf:
                    count_sheep += count_item.sheep
                else:
                    count_wolf += count_item.wolf
            else:
                count_sheep += count_item.sheep
                count_wolf += count_item.wolf

        return count_sheep, count_wolf


if __name__ == "__main__":
    n,m = [int(i) for i in input().split()]
    matrix = [input() for i in range(n)]

    sheepObj = Sheep(n,m,matrix)
    res = sheepObj.process()
    print(" ".join(map(str,res)))