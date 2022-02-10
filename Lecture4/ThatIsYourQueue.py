"""
That is Your Queue
Source: Uva   Time Limit: 3000ms   Memory Limit: 512MB
"""


def processQueue(p, c):
    arr = [i for i in range(1, min(p, c) + 1)]
    for _ in range(c):
        ch = input()
        if ch == "N":
            index = arr.pop(0)
            print(index)
            arr.append(index)
        else:
            index = int(ch.split()[1])
            size = len(arr)
            arr.append(index)
            for i in range(size):
                if arr[0] != index:
                    arr.append(arr.pop(0))
                else:
                    arr.pop(0)


if __name__ == "__main__":
    i_tc = 1
    while True:
        p,c = map(int, input().split())
        if p == c == 0:
            exit(0)
        print("Case {}:".format(i_tc))
        i_tc += 1
        processQueue(p,c)