"""
Monk and his friend
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left =  self.right = None


def checkValue(root, value):
    temp = root
    if temp is None:
        return False
    if temp.value == value:
        return True
    if temp.value > value:
        return checkValue(temp.left, value)
    return checkValue(temp.right, value)


def insert(root, value):
    temp = root
    if temp is None:
        return Node(value)

    if temp.value > value:
        temp.left = insert(temp.left, value)
    else:
        temp.right = insert(temp.right, value)
    return temp


if __name__ == "__main__":
    itc = int(input())
    for _ in range(itc):
        n,m = map(int, input().split())
        arr = list(map(int, input().split()))
        root = None
        for i in range(n):
            root = insert(root, arr[i])

        for i in range(m):
            st = checkValue(root, arr[i + n])
            if st:
                print("YES")
            else:
                print("NO")
                root = insert(root, arr[i + n])
