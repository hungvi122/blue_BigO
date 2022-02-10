"""
Contacts
Source: HackerRank   Time Limit: 1000ms   Memory Limit: 512MB
"""


class Trie:
    def __init__(self):
        self.words = {}
        self.count = 0


def insert(root, text):
    temp = root
    for ch in text:
        if ch not in temp.words:
            temp.words[ch] = Trie()
        temp = temp.words[ch]
        temp.count += 1


def search(root, query):
    temp = root
    for ch in query:
        if ch not in temp.words:
            return 0
        temp = temp.words[ch]
    return temp.count


if __name__ == "__main__":
    n = int(input())
    root = Trie()
    for _ in range(n):
        act, name = input().split()
        if act == "add":
            insert(root, name)
        else:
            count = search(root, name)
            print(count)