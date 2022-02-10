"""
Search Engine
Source: HackerEarth   Time Limit: 2000ms   Memory Limit: 512MB
"""

class Trie:
    def __init__(self, score):
        self.words = {}
        self.score = score
        self.isword = 0


def insert(root, text, score):
    temp = root
    for ch in text:
        if ch not in temp.words:
            temp.words[ch] = Trie(score)
        temp = temp.words[ch]
        if temp.score < score:
            temp.score = score
    temp.isword = 1


def search(root, query):
    temp = root
    for ch in query:
        if ch not in temp.words:
            return -1
        temp = temp.words[ch]
    return temp.score


if __name__ == "__main__":
    n,q = map(int, input().split())
    root = Trie(0)
    for _ in range(n):
        text, score = input().split()
        insert(root, text, int(score))

    for _ in range(q):
        query = input()
        score = search(root, query)
        print(score)
