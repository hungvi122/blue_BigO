class ParhaAndTea:
    """
    parha divided tea in the teapot for fiend, follow rule:
    women: the same x milliliters
    men: the same 2x milliliters
    and total tea divided is max of teapot
    INPUT:
    N (number men) W (milliliters in teapots)
    2N number separate by space, max milliliters in the cup.
    OUTPUT:
    number X milliliters teas can pour his friend.
    O TIME:
    O SPACE:
    """
    def process(self,n, k, arr_cup):
        arr = sorted(arr_cup)
        water = arr[0] if arr[0] * 2 < arr[n] else arr[n]/2
        return water * 3 * n if water * 3 * n < k else k


if __name__ == "__main__":
    n,k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    pashaObj = ParhaAndTea()
    res = pashaObj.process(n,k,arr)
    print(res)