"""
Penguins
Source: TimusOJ   Time Limit: 1000ms   Memory Limit: 512MB
"""

if __name__ == "__main__":
    n = int(input())
    mCount, iname = 0, ""
    mapNames = {}
    for _ in range(n):
        name = input()
        count = mapNames.get(name, 0) + 1
        mapNames[name] = count
        iname, mCount = (iname, mCount) if mCount >= count else (name, count)
    print(iname)

