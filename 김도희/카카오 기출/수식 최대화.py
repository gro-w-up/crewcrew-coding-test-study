#https://programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations

def calc(op, seq, exp):
    if exp.isdigit():
        return str(exp)
    else:
        if op[seq] == '*':
            split_exp = exp.split('*')
            temp = []
            for s in split_exp:
                temp.append(calc(op, seq+1, s))

            return str(eval('*'.join(temp)))

        if op[seq] == '+':
            split_exp = exp.split('+')
            temp = []
            for s in split_exp:
                temp.append(calc(op, seq + 1, s))
            return str(eval('+'.join(temp)))

        if op[seq] == "-":
            split_exp = exp.split("-")
            temp = []
            for s in split_exp:
                temp.append(calc(op, seq + 1, s))
            return str(eval("-".join(temp)))

def solution(expression):
    answer = 0
    op_rank = list(permutations(['*', '+', '-'], 3))

    for op in op_rank:
        result = abs(int(calc(op, 0, expression)))
        answer = max(answer, result)

    return answer