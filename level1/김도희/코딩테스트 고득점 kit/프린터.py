from collections import deque

def solution(priorities, location):
    answer = 0
    printer = deque([(priority, idx) for idx, priority in enumerate(priorities)])

    while printer:
        priority, idx = printer.popleft()

        if printer and priority < max(printer)[0]:
            printer.append((priority, idx))
        else:
            answer += 1
            if idx == location:
                break

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))