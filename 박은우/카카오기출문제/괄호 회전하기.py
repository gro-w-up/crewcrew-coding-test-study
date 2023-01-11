from collections import deque

def solution(s):

    print('------------------------------')
    # x(0 ≤ x < (s의 길이))
    s_len = len(s)
    queue = deque(s)

    # s를 어떻게 회전하더라도 올바른 괄호 문자열을 만들 수 없으므로, 0을 return 해야 합니다.
    answer = 0

    for i in range(s_len):
        if i > 0:
            left_char = queue.popleft()
            queue.append(left_char)

        print('queue = {}'.format(queue), end=' ')
        stack = []
        for q in queue:
            if stack:
                if stack[-1] == '(' and q == ')':
                    stack.pop()
                elif stack[-1] == '[' and q == ']':
                    stack.pop()
                elif stack[-1] == '{' and q == '}':
                    stack.pop()
                else:
                    stack.append(q)
            else:
                stack.append(q)

        print('stack = {}'.format(stack))
        if len(stack) == 0:
            answer += 1

    return answer


# expect 3
print(solution("[](){}"))
# expect 2
print(solution("}]()[{"))
# expect 0
print(solution("[)(]"))
# expect 0
print(solution("}}}"))