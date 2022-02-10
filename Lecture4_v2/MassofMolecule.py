"""
Mass Of molecule
Source: Spoj   Time Limit: 1000ms   Memory Limit: 512MB
CH(CO2H)3

"""

mapMolecule = {"C": 12, "H": 1, "O": 16}
if __name__ == "__main__":
    formulas = input()
    stack = []
    for ch in formulas:
        if ch in mapMolecule.keys():
            stack.append(mapMolecule.get(ch))
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            tmp = 0
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop()
            stack.append(tmp)
        else: # number
            stack.append(stack.pop() * int(ch))

    sizeOfMolecule = 0
    while len(stack) > 0:
        sizeOfMolecule += stack.pop()
    print(sizeOfMolecule)

