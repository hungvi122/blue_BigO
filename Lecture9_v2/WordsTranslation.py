"""
Word Transformation
Source: Big-O   Time Limit: 1000ms   Memory Limit: 512MB
"""
def checkword(s1, s2):
    if len(s1) != len(s2):
        return False
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count == 2:
                return False
    return True


def bfs(s, e, n, graph):
    visited = [False] * n
    visited[s] = True
    queue = [(s, 0)]
    while len(queue) > 0:
        u, w = queue.pop(0)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, w + 1))
                if v == e:
                    return w + 1
    return 0


def process():
    words = []
    while True:
        d = input()
        if d != '*':
            words.append(d)
        else:
            break

    size = len(words)
    graph = [[] for _ in range(size)]
    for i in range(size-1):
        for j in range(i + 1, size):
            if checkword(words[i], words[j]):
                graph[i].append(j)
                graph[j].append(i)

    while True:
        try:
            params = input()
            if len(params) == 0:
                break
            text1, text2 = params.split()
            res = bfs(words.index(text1), words.index(text2), size, graph)
            print(text1, text2, res)
        except EOFError:
            break


if __name__ == "__main__":
    iTC = int(input())
    for i in range(iTC):
        if i == 0:
            input()
        process()
        if i < iTC - 1:
            print()