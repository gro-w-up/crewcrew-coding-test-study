def solution(array, commands):
    answer = []

    for command in commands:
        start = command[0] - 1
        end = command[1]
        target = command[-1] - 1

        answer.append(sorted(array[start:end])[target])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))