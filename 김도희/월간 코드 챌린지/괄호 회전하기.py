from collections import deque

def check_right_bracket(s):
    stack = deque()
    for ch in s:
        if ch in {'(', '{', '['}:
            stack.append(ch)
        elif not stack or stack.pop() + ch not in {'()', '{}', '[]'}:
            return False
    return len(stack) == 0

def solution(s):
    answer = 0
    s = deque(s)

    for idx in range(len(s)):
        s.rotate(-1)
        if check_right_bracket(s):
            answer += 1

    return answer

print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))