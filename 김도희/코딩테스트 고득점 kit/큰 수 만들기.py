def solution(number, k):
    answer = []

    for val in number:
        while k > 0 and answer and answer[-1] < val:
            answer.pop()
            k -= 1
        answer.append(val)

    return ''.join(answer[:len(answer) - k])

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))