"""
Distinct Count
Source: HackerEarth   Time Limit: 1000ms   Memory Limit: 512MB
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def checkNotExists(root, value):
    temp = root
    if temp is None:
        return True
    if temp.value == value:
        return False
    if temp.value > value:
        return checkNotExists(temp.left, value)
    return checkNotExists(temp.right, value)


def insertValue(root, value):
    temp = root
    if temp is None:
        return Node(value)
    if temp.value > value:
        temp.left = insertValue(temp.left, value)
    else:
        temp.right = insertValue(temp.right, value)
    return temp


if __name__ == "__main__":
    iTC = int(input())
    for _ in range(iTC):
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))
        root = None
        size = 0
        for i in arr:
            if checkNotExists(root, i):
                size += 1
                root = insertValue(root, i)
        if x == size:
            print("Good")
        elif x < size:
            print("Average")
        else:
            print("Bad")