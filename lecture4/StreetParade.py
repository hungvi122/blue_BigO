class StreetParade:
    """
    sort the struck in the other. two vehicle can pass other, it can use the side street to other struck
    INPUT:
    N testcase,
    N-truck arbitrary order. No more 1000 participate. input end with 0
    OUTPUT:
    YES --> can sort, NO when opposite.
    """

    def __init__(self, n, struck_arr):
        self.n = n
        self.struct_arr = struck_arr

    def process(self):
        start = 1
        stack = []
        while len(self.struct_arr) > 0:
            if self.struct_arr[0] == start:
                self.struct_arr.pop(0)
                start += 1
            elif len(stack) > 0 and stack[-1] == start:
                stack.pop()
                start += 1
            else:
                stack.append(self.struct_arr.pop(0))

        while len(stack) > 0:
            if stack[-1] == start:
                stack.pop()
                start += 1
            else:
                return False
        if start > self.n:
            return True
        return False


if __name__ == "__main__":

    while True:
        n = int(input())
        if n == 0:
            exit(0)
        arr_struck = [int(i) for i in input().split()]
        streetObj = StreetParade(n, arr_struck)
        res = streetObj.process()
        if res:
            print("yes")
        else:
            print("no")
