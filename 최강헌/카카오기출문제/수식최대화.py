import re
import itertools


def solution(expression):
    #    expression = re.sub('([-+*])',' \g<1> ', expression).split()
    operators = list(itertools.permutations(['-', '+', '*'], 3))
    print(operators)
    expression = re.split('([-+*])', expression)
    results = []

    # for operator in operators:
    #     for op in operator:
    #         while op in expression:
    #             idx = expression.index(op)
    #             expression[idx - 1] = str(eval(expression[idx - 1] + op + expression[idx + 1]))
    #             del expression[idx:idx + 2]
    #         results.append(expression)

    for operator in operators:
        exp = expression[:]
        for op in operator:
            while op in exp:
                idx = exp.index(op)
                exp[idx - 1] = str(eval(exp[idx - 1] + op + exp[idx + 1]))
                del exp[idx:idx + 2]
        results.append(abs(int(exp[0])))

    return max(results)


solution("100-200*300-500+20")
