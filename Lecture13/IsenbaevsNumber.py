"""
Isenbaev's Number
Source: TimusOJ   Time Limit: 1000ms   Memory Limit: 512MB
"""

if __name__ == "__main__":
    n = int(input())
    graphNames = dict()
    for _ in range(n):
        pNames = input().split()
        for name in pNames:
            arr = graphNames.get(name, [])
            arr.extend(pNames)
            graphNames[name] = arr
    mapResult = dict()
    names = list(graphNames.keys())
    names.sort()
    queue = []
    if "Isenbaev" in names:
        queue.append((0, "Isenbaev"))
        mapResult["Isenbaev"] = 0
    while len(queue) > 0:
        w, name = queue.pop(0)
        for v in graphNames[name]:
            if mapResult.get(v, n) > w + 1:
                mapResult[v] = w + 1
                queue.append((w + 1, v))

    for name in names:
        relate = mapResult.get(name, "undefined")
        print(name, relate)