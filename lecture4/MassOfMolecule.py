class MassOfMolecule:
    """
    molecule contain H(1), C(12), O(16)
    format mocule: COOOH, CH(OH), CH(CO2H)3... CxHyOz : x,y,z (2 <=x,y,z<=9)
    INPUT:
    Format molecule.
    OUTPUT:
    mass of molecule.
    O time : len(molecule)
    O space: len(molecule)
    """

    def process(self, molecule):
        stack = []
        mass_size = 0
        map_mass_atom = {'H': '1', 'C': '12', 'O': '16'}

        for i in molecule:
            if i == '(':
                stack.append(i)
            elif '2' <= i <= '9':
                pre_atom = int(stack.pop()) * int(i)
                stack.append(str(pre_atom))
            elif i == ')':
                pre_mass_group = 0
                while len(stack) > 0 and stack[-1] != '(':
                    pre_mass_group += int(stack.pop())
                stack.pop()
                stack.append(str(pre_mass_group))
            else:  # case H, C, O
                stack.append(map_mass_atom[i])

        while len(stack) > 0:
            mass_size += int(stack.pop())
        return mass_size


if __name__ == "__main__":
    molecule = input()
    massMoleculeObj = MassOfMolecule()
    res = massMoleculeObj.process(molecule)
    print(res)