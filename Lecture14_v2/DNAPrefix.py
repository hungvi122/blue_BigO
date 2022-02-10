"""
DNA prefix
Source: LightOJ   Time Limit: 5000ms   Memory Limit: 512MB
"""


class Trie:
    def __init__(self, lengh, count):
        self.child = {}
        self.len = lengh
        self.count = count


def insert(root, text):
    temp = root
    res = 0
    for i in range(len(text)):
        ch = text[i]
        if ch not in temp.child:
            temp.child[ch] = Trie(i + 1, 0)
        temp = temp.child[ch]
        temp.count += 1
        res = max(res, temp.len * temp.count)
    return res


def process(tc):
    n = int(input())
    root = Trie(0,0)
    maxRes = 0
    for _ in range(n):
        res = insert(root, input())
        maxRes = max(res, maxRes)
    print("Case {}: {}".format(tc, maxRes))


if __name__ == "__main__":
    itc = int(input())
    for i in range(itc):
        process(i + 1)