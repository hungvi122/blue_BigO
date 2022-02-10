class BusinessTrip:
    """
    Petya' parent has a trip in whole year, and assign he task grow plant.
    Each month Petya watering plant and plant grow exact x centimeters in month
    Petya make as least total grow: K centimeters.
    INPUT:
    K centimeters.
    12 month with x centimeters in grow
    OUTPUT:
    Minimum number month Pytya watering, or -1 if conn't grow k centimeters
    O TIME: 1 (12
    O SPACE: 1
    """
    def process(self, k, grows_high):
        arr = sorted(grows_high, reverse=True)
        count = 0
        if k == 0:
            return 0
        for grow_x in arr:
            k -= grow_x
            count += 1
            if k <= 0:
                return count
        return -1


if __name__ == "__main__":
    businessObj = BusinessTrip()
    k = int(input())
    arr = [int(i) for i in input().split()]
    res = businessObj.process(k, arr)
    print(res)