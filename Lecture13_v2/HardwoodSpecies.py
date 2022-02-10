"""
Hardwood species
Source: UVA   Time Limit: 3000ms   Memory Limit: 512MB
"""

if __name__ == "__main__":
    itc = int(input())
    for i in range(itc):
        if i == 0:
            input()
        else:
            print()
        mapNames = {}
        total = 0
        while True:
            try:
                name = input()
                if name == "":
                    break
                total += 1
                count = mapNames.get(name, 0)
                mapNames[name] = count + 1
            except EOFError:
                break
        names = list(mapNames.keys())
        names.sort()

        for name in names:
            print(name, "{:.4f}".format(mapNames[name]/total * 100))
