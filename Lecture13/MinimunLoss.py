"""
Minimum loss
Source: HackerRank   Time Limit: 1000ms   Memory Limit: 512MB
"""

class Node:
    def __init__(self,index, value):
        self.i = index
        self.v = value
        self.left = self.right = None


def insert(root, index, value):
    temp = root
    if temp is None:
        return Node(index, value)
    if temp.v > value:
        temp.left = insert(temp.left, index, value)
    else:
        temp.right = insert(temp.right, index, value)
    return temp


def traceInorder(root, arrItem):
    if root is None:
        return
    if root.left is not None:
        traceInorder(root.left, arrItem)
    arrItem.append((root.i, root.v))
    if root.right is not None:
        traceInorder(root.right, arrItem)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    root = None
    for i in range(n):
        root = insert(root, i, arr[i])

    arrItem = []
    traceInorder(root, arrItem)
    minValue = 10 ** 16
    for i in range(1, n):
        dist = arrItem[i][1] - arrItem[i-1][1]
        if arrItem[i-1][0] > arrItem[i][0]:
            minValue = min(minValue, dist)
    print(minValue)