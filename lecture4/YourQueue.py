class HealthCareQueue:
    """
    1-N patient, when exp - E , the obj move on the queue.

    INPUT:
    P-N: P number patient, N number command process.
    N input
    OUTPUT:
    The order patient
    """
    def process(self, P, arr_command):
        queue = [i for i in range(1, min(P, len(arr_command)) + 1)]
        res = []
        for command in arr_command:
            if command == 'N':
                k = queue.pop(0)
                res.append(k)
                queue.append(k)
            else:
                size_queue = len(queue)
                ex = int(command.split()[1])
                queue.append(ex)
                for i in range(size_queue):
                    k = queue.pop(0)
                    if k == ex:
                        continue
                    queue.append(k)

        return res


if __name__ == "__main__":
    healthQueue = HealthCareQueue()
    i_case = 0
    while True:
        P,N = [int(i) for i in input().split()]
        if P == 0 and N == 0:
            exit(0)
        arr_command = [input() for i in range(N)]
        i_case += 1
        res = healthQueue.process(P,arr_command)
        print("Case {}:".format(i_case))
        for i in res:
            print(i)



