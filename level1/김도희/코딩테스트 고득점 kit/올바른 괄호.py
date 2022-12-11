from collections import deque

def solution(s):
    if s[0] == ')':
        return False

    s = deque(s)
    stack = []

    while s:
        checked = s.popleft()

        if checked == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(checked)

    return False if stack else True


print(solution("()()"))
print(solution("(())()"	))
print(solution(")()("))
print(solution("(()("))