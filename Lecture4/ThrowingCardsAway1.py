"""
Throwing Cards Away 1
Source: Uva   Time Limit: 3000ms   Memory Limit: 512MB
7
19
10
6
0
"""


def checkCard(n):
    arr = [i for i in range(1, n + 1)]
    arr_pick = []
    while len(arr) > 1:
        arr_pick.append(arr.pop(0))
        arr.append(arr.pop(0))
    return arr_pick, arr[0]


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            exit(0)
        res = checkCard(n)
        if len(res[0]) > 0:
            print("Discarded cards: {}".format(", ".join(map(str, res[0]))))
        else:
            print("Discarded cards:")
        print("Remaining card: {}".format(res[1]))
