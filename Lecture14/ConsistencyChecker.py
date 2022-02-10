"""
Consistency Checker
Source: LightOJ   Time Limit: 500ms   Memory Limit: 512MB
"""


class Trie:
    def __init__(self):
        self.child = {}
        self.isWord = False


def insert(root, text):
    temp = root
    for ch in text:
        if ch not in temp.child:
            temp.child[ch] = Trie()
        temp = temp.child[ch]
        if temp.isWord:
            return True
    temp.isWord = True
    if len(temp.child) > 0:
        return True
    return False


def process(tc):
    n = int(input())
    root = Trie()
    checkPrefix = False
    for _ in range(n):
        if not checkPrefix:
            checkPrefix = insert(root, input())
        else:
            input()
    print("Case {}: {}".format(tc, "NO" if checkPrefix else "YES"))


if __name__ == "__main__":
    itc = int(input())
    for i in range(itc):
        process(i + 1)