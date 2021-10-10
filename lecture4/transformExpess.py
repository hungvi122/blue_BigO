from _thread import exit


class TransformExpress:
    """
    algebraic expression with brackets into RPN form.
    operator: +-*/^
    a-z
    INPUT:
    T number testcase.
    t -testcase.
    OUTPUT:
    RPN express
    """

    def process(self, algebraic_express):
        res = ""
        stack = []
        express = ['+', '-', ' ', '*', '/', ' ', '^']
        for i in algebraic_express:
            if 'a' <= i <= 'z':
                res += i
            elif i == '(' or i == '^' or len(stack) == 0:
                stack.append(i)
            elif i == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    res += stack[-1]
                    stack.pop()
                stack.pop()
            else:
                while len(stack) > 0 and (stack[-1] in express) and express.index(stack[-1]) > express.index(i) + 1:
                    res += stack[-1]
                    stack.pop()
                stack.append(i)

        while len(stack) > 0:
            res += stack.pop()
        return res


if __name__ == "__main__":
    n = int(input())
    tranformObj = TransformExpress()
    for i in range(n):
        express = input()
        res = tranformObj.process(express)
        print(res)
