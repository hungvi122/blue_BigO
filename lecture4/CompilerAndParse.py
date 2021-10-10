class CompilerAndParse:
    """
    lira design new language with using <,>
    rule: a < symbol must always have a corresponding >
    INPUT:
    N number testcase.
    n -line testcase
    OUTPUT:
    print max size prefix valid or 0 if no prefix valid
    example: 3
    <<>>
    ><
    <>>>
    O TIME:
    O SPACE:
    """
    def processs(self, expression):
        stack = []
        max_longest_prefix = 0

        for i in range(len(expression)):
            if expression[i] == '<':
                stack.append(expression[i])
            else:
                if len(stack) > 0 and stack[-1] == '<':
                    stack.pop()
                else:
                    return max_longest_prefix
                if len(stack) == 0:
                    max_longest_prefix = i + 1

        return max_longest_prefix


if __name__ == "__main__":
    n = int(input())
    expressObj = CompilerAndParse()
    for i in range(n):
        express = input()
        res = expressObj.processs(express)
        print(res)

