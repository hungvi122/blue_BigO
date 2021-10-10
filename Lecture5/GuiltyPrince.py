class GuiltyPrince:
    """
    Shahjahan is price:
    share edge, move land
    count total land
    input:
    T testcase
    W,H , W,H <= 20
    . land, # water, @ position prince
    """
    def __init__(self, height, width, matrixG):
        self.H = height
        self.W = width
        self.MATRIX = matrixG

    def process(self):
        start = 0
        visited = [False] * self.W * self.H
        queue = []
        count = 1
        graph = [[] for i in range(self.W * self.H)]
        for i in range(self.H):
            for j in range(self.W):
                if self.MATRIX[i][j] != '#':
                    if i - 1 >= 0 and self.MATRIX[i-1][j] != '#':
                        graph[i*self.W + j].append((i-1)*self.W + j)
                    if i + 1 < self.H and self.MATRIX[i+1][j] != '#':
                        graph[i*self.W + j].append((i+1)*self.W + j)
                    if j - 1 >= 0 and self.MATRIX[i][j-1] != '#':
                        graph[i*self.W + j].append(i*self.W + j - 1)
                    if j + 1 < self.W and self.MATRIX[i][j+1] != '#':
                        graph[i*self.W + j].append(i*self.W + j + 1)
                if self.MATRIX[i][j] == '@':
                    if start == 0:
                        start = i * self.W + j
                    else:
                        return -1

        queue.append(start)
        visited[start] = True

        while len(queue) > 0:
            u = queue.pop(0)
            if len(graph[u]) == 0:
                continue
            for v in graph[u]:
                if visited[v] is False:
                    visited[v] = True
                    count += 1
                    queue.append(v)
        return count


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        w,h = [int(i) for i in input().split()]
        matrix = [input() for j in range(h)]

        guiltyObj = GuiltyPrince(h,w,matrix)
        res = guiltyObj.process()
        print("Case {}: {}".format(i + 1, res))