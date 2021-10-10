class Chores:
    """
    Petya and Vasya arr brothers, today their parens left the home.
    and give them task housework.
    With n task and each task has difficult level.
    Petya decided doing A task with difficult level >=X.
    INPUT:
    N,A,B : number chores, A task petya B task Vasya.
    N level task, separate by space.
    OUTPUT:
    number ways choose X, or 0 if no way.
    O TIME: NLog(N)
    O SPACE: N (arr sorted).
    """
    def process(self, n, a, b, chores):
        arr = sorted(chores)
        return arr[b] - arr[b-1]


if __name__ == "__main__":
    n,a,b = [int(i) for i in input().split()]
    arr = [int(str_val) for str_val in input().split()]
    choresObj = Chores()
    result = choresObj.process(n,a,b,arr)
    print(result)