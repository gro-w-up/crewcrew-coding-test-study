from collections import deque


def solution(s):
    queue = deque(s)  # 큐 생성
    cnt = 0  # 카운트 초기화

    # 문자열 길이만큼 반복
    for i in range(len(s)):
        tmp = queue.popleft()
        queue.append(tmp)
        s = ''.join(queue)

        while '[]' in s or '()' in s or '{}' in s:
            if '[]' in s:
                s = s.replace('[]', '')
            if '()' in s:
                s = s.replace('()', '')
            if '{}' in s:
                s = s.replace('{}', '')

        if s == '': cnt += 1
    return cnt


solution("[](){}")
