def solution(s):

    if len(s) // 2 == 0:
        return False

    count = 0
    for character in s:
        # print(character, ' : ', count)
        if character == '(':
            count += 1
        if character == ')':
            count -= 1
        if count < 0:
            break

    return count == 0

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))

"""
접근 및 풀이 방법
    문제 단순화
        - "()()" 또는 "(())()" 는 올바른 괄호, ")()(" 또는 "(()(" 는 올바르지 않은 괄호
        - '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true
    풀이 계획
        - 문자 열을 반복문을 돌려 첫문자부터 검증을 시작한다.
        - '('인 경우 +1, ')'인 경우 -1
        - 만약 검증 숫자가 0보다 작은 경우 반복문 수행을 멈춘다.
        - count가 0이라면 올바른 괄호를 의미하는 true를 반환하고, 그렇지 않은 경우 초기값 False를 반환한다.   
"""