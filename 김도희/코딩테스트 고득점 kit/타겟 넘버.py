#https://programmers.co.kr/learn/courses/30/lessons/43165
from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, 0))

    while q:
        current_sum, num_idx = q.popleft()
        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            q.append((current_sum + number, num_idx+1))
            q.append((current_sum - number, num_idx + 1))

    return answer