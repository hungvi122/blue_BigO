class ValidateTheMaze:
    """
    Maze had only 2 point open edge
    INPUT:
    M,N size of maze
    # is wall, . is space
    OUTPUT: valid or invalid
    """
    def __init__(self, M, N, MATRIX):
        self.m = M
        self.n = N
        self.matrix = MATRIX

    def process(self):
        graph = [[] for i in range(m*n)]
        e_point = []
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and self.matrix[i][j] == '.':
                    e_point.append(i*n +j)
                if self.matrix[i][j] == '.':
                    if i - 1 >= 0 and self.matrix[i-1][j] == '.':
                        graph[i*n+j].append((i-1)*n + j)
                    if i + 1 < m and self.matrix[i+1][j] == '.':
                        graph[i*n+j].append((i+1)*n + j)
                    if j - 1 >= 0 and self.matrix[i][j-1] == '.':
                        graph[i*n+j].append(i*n + j - 1)
                    if j + 1 < n and self.matrix[i][j+1] == '.':
                        graph[i*n+j].append(i*n + j + 1)

        if len(e_point) != 2:
            return "invalid"
        s,f = e_point[0], e_point[1]

        queue = []
        visited = [False] * m * n
        visited[s] = True
        queue.append(s)
        while len(queue) > 0:
            u = queue.pop(0)
            if len(graph[u]) > 0:
                for v in graph[u]:
                    if v == f:
                        return "valid"
                    elif visited[v] is False:
                        visited[v] = True
                        queue.append(v)

        return "invalid"


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        m,n = [int(j) for j in input().split()]
        graph_des = [input() for i in range(m)]
        # print("testcase: {i}", i)
        validObj = ValidateTheMaze(m,n, graph_des)
        res = validObj.process()
        print(res)


