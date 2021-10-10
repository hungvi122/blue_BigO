class DevuTheDumbGuy:
    """
    Devu is learning slow.
    and when he he teach subject, each subject has X chapter, the time teach reduce 1 hour. , and time learning not less than 1 hour.
    WE should choose the order chapter for Devu learning with short time.
    INPUT:
    N,X: number subject and time learn first chapter.
    N number chapter of subject.
    OUPUT:
    Shorted time learn all subject.
    O TIME: NLog(N)
    O SPACE: N (arr sorted)
    """

    def process(self, time, subjects):
        arr = sorted(subjects)
        result = 0
        for i in arr:
            result += time * i
            time = time if time == 1 else time - 1
        return result


if __name__ == "__main__":
    n,time = [int(i) for i in input().split()]
    arr = [int(str_val) for str_val in input().split()]
    devuLearnObj = DevuTheDumbGuy()
    result = devuLearnObj.process(time, arr)
    print(result)