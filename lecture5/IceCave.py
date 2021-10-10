class IceCave:
    """
    rectangle square grid of n rows and m column
    X: describe crack ice, . describe intact ice
    You move from r1,c1 to r2,c2. if r2 . move dup
    INPUT:
    N, M.
    Matrix
    OUTPUT: YES, NO
    """
    def __init__(self, n, m, matrix, s, f):
        self.n = n
        self.m = m
        self.matrix = matrix
        self.s = s
        self.f = f


    def process(self):
        queue = []
        visited = [False] * self.m * self.n
        start = (self.s[0]-1) * self.m + self.s[1]-1
        finish = (self.f[0]-1)*self.m + self.f[1]-1
        graph = [[] for i in range(self.n * self.m)]
        can_move = False
        for i in range(self.n):
            for j in range(self.m):
                if i != self.f[0]-1 or j != self.f[1]-1:
                    if i - 1 >= 0 and (self.matrix[i - 1][j] != 'X' or (i - 1 == self.f[0] - 1 and j == self.f[1] - 1)):
                        graph[i * self.m + j].append((i - 1) * self.m + j)
                    if i + 1 < self.n and (
                            self.matrix[i + 1][j] != 'X' or (i + 1 == self.f[0] - 1 and j == self.f[1] - 1)):
                        graph[i * self.m + j].append((i + 1) * self.m + j)
                    if j - 1 >= 0 and (self.matrix[i][j - 1] != 'X' or (i == self.f[0] - 1 and j - 1 == self.f[1] - 1)):
                        graph[i * self.m + j].append(i * self.m + j - 1)
                    if j + 1 < self.m and (
                            self.matrix[i][j + 1] != 'X' or (i == self.f[0] - 1 and j + 1 == self.f[1] - 1)):
                        graph[i * self.m + j].append(i * self.m + j + 1)
                else:
                    count_intact=0
                    if i - 1 >= 0 and self.matrix[i - 1][j] == '.':
                        count_intact += 1
                    if i + 1 < self.n and self.matrix[i + 1][j] == '.':
                        count_intact += 1
                    if j - 1 >= 0 and self.matrix[i][j - 1] == '.':
                        count_intact += 1
                    if j + 1 < self.m and self.matrix[i][j + 1] == '.':
                        count_intact += 1
                    if self.matrix[i][j] == 'X' and count_intact > 0:
                        can_move = True
                    if self.matrix[i][j] == '.' and count_intact > 1:
                        can_move = True

        if can_move is False:
            return "NO"
        queue.append(start)
        visited[start] = True
        while len(queue) > 0:
            u = queue.pop(0)

            if len(graph[u]) == 0:
                continue
            for v in graph[u]:
                if visited[v] is False:
                    if v == finish:
                        return "YES"
                    visited[v] = True
                    queue.append(v)

        return "NO"


if __name__ == "__main__":
    n,m = [int(i) for i in input().split()]
    matrix = [input() for i in range(n)]

    s = [int(i) for i in input().split()]
    f = [int(i) for i in input().split()]
    iceObj = IceCave(n,m,matrix,s,f)
    res = iceObj.process()
    print(res)
