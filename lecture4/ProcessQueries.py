class ProcessingQueries:
    """
    1 thread processor for process tasks queue
    rule: server free , take first task and process.
    server busy, put task in queue, if queue full, drop task.
    INPUT:
    N,B: number queries and max queue size.
    n -line describe time arrive and time process.
    OUTPUT: print time task done process, or -1 if task drop.
    O TIME: N
    O SPACE: N
    """
    def process(self, n, b, tasks):
        time_server = 0
        queue = []
        res = [-1] * n
        index = 0
        while index < len(tasks) or len(queue) > 0:
            # take task from tasks or queue
            i_task = None
            if len(queue) == 0 and index < len(tasks):
                i_task = (tasks[index], index)
                index += 1
            elif len(queue) > 0:
                i_task = queue.pop(0)

            # process task
            task = i_task[0]
            i = i_task[1]
            time_server = max(time_server, task[0])
            time_server += task[1]
            res[i] = time_server

            # update queue
            for i in range(index, n):
                if time_server > tasks[i][0]:
                    if len(queue) < b:
                        queue.append((tasks[i], i))
                    index += 1
                else:
                    break

        return res


if __name__ == "__main__":
    n,b = [int(i) for i in input().split()]
    tasks = []
    for i in range(n):
        tasks.append([int(j) for j in input().split()])

    processObj = ProcessingQueries()
    res = processObj.process(n, b, tasks)

    print(" ".join(map(str, res)))



