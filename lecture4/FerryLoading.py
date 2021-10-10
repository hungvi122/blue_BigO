class FerryLoading:
    """
    Ferry move between two bank of river.
    car can loading on ferry and move to the other bank.
    ferry move when carry as least car, or car in the other bank. otherwise ferry idle.
    INPUT:
    C: number testcase.
    N,T,M: N: max total car loading on ferry., T time move between two bank of river, M number car arrive
    M-line car arrive : time-arrive, bank river
    OUTPUT:
    Each test case, print time car unloaded at the opposite bank. blank line between testcase.
    O TIME: M
    O SPACE: M
    """

    def process(self, N, T,M, arr_car_arrive):
        car_left_queue = [(i, int(arr_car_arrive[i].split()[0])) for i in range(M) if
                          arr_car_arrive[i].split()[1] == 'left']
        car_right_queue = [(i, int(arr_car_arrive[i].split()[0])) for i in range(M) if
                           arr_car_arrive[i].split()[1] == 'right']
        time_ferry = 0
        bank_river = False  # left: false, right: true
        res = [0] * len(arr_car_arrive)
        while len(car_left_queue) > 0 or len(car_right_queue) > 0:
            new_bank_river = bank_river
            queue_queries = None

            if bank_river is False:
                if len(car_right_queue) == 0 or (len(car_left_queue) > 0 and car_left_queue[0][1] <= time_ferry) \
                        or (len(car_left_queue) > 0 and car_left_queue[0][1] <= car_right_queue[0][1]):
                    new_bank_river = False
                    queue_queries = car_left_queue
                else:
                    new_bank_river = True
                    queue_queries = car_right_queue
            else:
                if len(car_left_queue) == 0 or (len(car_right_queue) > 0 and car_right_queue[0][1] <= time_ferry) \
                        or (len(car_right_queue) > 0 and car_right_queue[0][1] <= car_left_queue[0][1]):
                    new_bank_river = True
                    queue_queries = car_right_queue
                else:
                    new_bank_river = False
                    queue_queries = car_left_queue

            time_ferry = max(time_ferry, queue_queries[0][1])
            if new_bank_river != bank_river:
                time_ferry += T

            bank_river = new_bank_river

            queue_car_loading = []
            # loading car
            while len(queue_queries) > 0 and len(queue_car_loading) < N:
                if queue_queries[0][1] <= time_ferry:
                    queue_car_loading.append(queue_queries.pop(0))
                else:
                    break

            # unload
            time_ferry += T
            for i in queue_car_loading:
                res[i[0]] = time_ferry
            bank_river = not bank_river
        return res


if __name__ == "__main__":
    n = int(input())
    ferryObj = FerryLoading()
    for i_test in range(n):
        N,T,M = [int(i) for i in input().split()]
        car_arrive = [input() for i in range(M)]
        res = ferryObj.process(N,T,M,car_arrive)
        for i in res:
            print(i)
        if i_test < n - 1:
            print("")