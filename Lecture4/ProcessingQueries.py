"""
Processing Queries
"""


class Task:
    def __init__(self, i, start, execTime):
        self.index = i
        self.start = start
        self.execTime = execTime


if __name__ == "__main__":
    n, b = map(int, input().split())
    timeServer = 0
    queue = []
    res = [-1 for _ in range(n)]
    index = 0
    while index < n or len(queue) > 0:
        task = None
        newTask = None
        if index < n:
            timeIn, timeExec = map(int, input().split())
            newTask = Task(index, timeIn, timeExec)
            index += 1
        if newTask is not None and newTask.start < timeServer:
            if len(queue) < b:
                queue.append(newTask)
            continue

        if len(queue) == 0:
            task = newTask
        else:
            task = queue.pop(0)
            if newTask is not None:
                queue.append(newTask)

        if task is not None:
            timeServer = max(task.start, timeServer) + task.execTime
            res[task.index] = timeServer

    print(" ".join(map(str, res)))
