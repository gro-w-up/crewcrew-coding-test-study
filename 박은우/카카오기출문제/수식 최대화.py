from itertools import permutations


def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))


def calculate(expression, op):
    array = []
    temp = ""

    # 문자열에서 연산자와 숫자 분리
    for i in expression:
        # print('temp = {}, i = {}, i.isdigit = {}'.format(temp, i, i.isdigit()))
        if i.isdigit():
            temp += i
        else:
            array.append(temp)
            array.append(i)
            temp = ""
    array.append(temp)

    # 연산자 루프
    for o in op:
        stack = []
        while len(array) != 0:
            temp = array.pop(0)
            if temp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(temp)
        array = stack

    return abs(int(array[0]))


def solution(expression):
    # 조합식 리스트 만들기
    op = list(permutations(['+', '-', '*'], 3))
    print('op = {}'.format(op))
    result = []
    # 만들어진 조합식 리스트 만큼 계산
    for i in op:
        result.append(calculate(expression, i))
    return max(result)

# expect 60420
print(solution("100-200*300-500+20"))
# expect 300
print(solution("50*6-3*2"))