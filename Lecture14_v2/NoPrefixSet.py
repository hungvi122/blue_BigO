"""
No Prefix Set
Nguồn bài: HackerRank   Giới hạn thời gian: 2000ms   Giới hạn bộ nhớ: 512MB
"""


class Trie:
    def __init__(self):
        self.words = {}
        self.isWord = 0


def insert(root, text):
    temp = root
    for ch in text:
        if ch not in temp.words:
            temp.words[ch] = Trie()
        temp = temp.words[ch]
        if temp.isWord:
            return True
    temp.isWord += 1
    if len(temp.words) > 0:
        return True
    return False


if __name__ == "__main__":
    n = int(input())
    root = Trie()
    checkPrefix = False
    for _ in range(n):
        text = input()
        checkPrefix = insert(root, text)
        if checkPrefix:
            print("BAD SET")
            print(text)
            exit(0)
    print("GOOD SET")