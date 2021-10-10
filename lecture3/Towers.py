class Tower:
    """
    little Vasya receive a task builder.
    kit contain several wooden bars, length of them unknown.
    The bar can put on the top if their length are the same.
    INPUT:
    N number Bar.
    N number separate by space.
    OUTPUT:
    height of largest tower and their number total tower.
    O TIME: NLog(N)
    O SPACE: Max Arr_Wooden + 1
    """

    def process(self, arr_wooden):
        arr = sorted(arr_wooden)
        freq = [0] * (max(arr) + 1)
        max_high, num_tower = 0, 0

        for i in arr:
            if freq[i] == 0:
                num_tower += 1
            freq[i] += 1
            max_high = max_high if max_high >= freq[i] else freq[i]

        return max_high,num_tower


if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]
    towerObj = Tower()
    res = towerObj.process(arr)
    print(res[0], res[1])