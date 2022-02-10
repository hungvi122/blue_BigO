"""
Old Berland language
Source: Codeforces   Time Limit: 2000ms   Memory Limit: 512MB
"""
import sys
sys.setrecursionlimit(1500)


class Trie:
    def __init__(self):
        self.words = {}
        self.isword = 0


def insert(root, text, level, length):
    temp = root
    if level == length:
        temp.isword = 1
        return True, text
    isNext = False
    for c in range(2):
        if c not in temp.words:
            temp.words[c] = Trie()
        if temp.words[c].isword == 0:
            flag, text = insert(temp.words[c], text + str(c), level + 1, length)
            if flag:
                if len(temp.words) == 2 and temp.words[0].isword == 1 and temp.words[1].isword == 1:
                    temp.isword = 1
                isNext = True
                break
    if not isNext:
        return False, ""
    return True, text


if __name__ == "__main__":
    n = int(input())
    arrSrc = list(map(int, input().split()))
    arrTemp = [(arrSrc[i], i) for i in range(n)]
    arrTemp.sort()
    res = []
    root = Trie()
    for length, index in arrTemp:
        flag, text = insert(root, "", 0, length)
        if not flag:
            print("NO")
            exit(0)
        else:
            res.append((index, text))
    res.sort()
    print("YES")
    for index,text in res:
        print(text)