def sort_arr():
    n = int(input())
    arr_str = input().split()
    arr = [int(i) for i in arr_str]
    start, end = -1, n
    is_increase = True
    count = 0
    for i in range(n-1):
        if arr[i] < arr[i+1] and is_increase and count == 0:
            start = i
        elif arr[i] > arr[i + 1] and is_increase:
            is_increase = False
            count += 1
            if count == 2:
                print("no")
                return
        elif arr[i] < arr[i + 1] and is_increase is False:
            end = i
            is_increase = True

    if count == 0:
        print("yes")
        print(1, 1)
        return
    else:
        if start == -1 and end == n:
            print("yes")
            print(1, n)
            return
        elif start == -1:
            if arr[0] <= arr[end + 1]:
                print("yes")
                print(1, end + 1)
                return
        elif end == n:
            if arr[start] <= arr[end-1]:
                print("yes")
                print(start + 2, n)
                return
        elif arr[start] <= arr[end] and arr[start + 1] <= arr[end + 1]:
            print("yes")
            print(start + 2, end + 1)
            return

        print("no")

sort_arr()