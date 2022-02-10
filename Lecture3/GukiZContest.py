class GuikiContest:
    """
    Guiki like programing, he prepare the contest.
    In contest with n student participant. student has same result has same rank ith.
    INPUT:
    N number student.
    N number result separate by space.
    OUTPUT:
    print Rank each student.
    O TIME: NLog(N)
    O SPACE: N
    """
    def process(self, contest):
        arr_sorted = sorted(contest, reverse=True)
        arr_res = []
        for i in contest:
            index = arr_sorted.index(i)
            arr_res.append(index + 1)
        return arr_res


if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]
    guikiObj = GuikiContest()
    res = guikiObj.process(arr)
    print(" ".join(map(str, res)))