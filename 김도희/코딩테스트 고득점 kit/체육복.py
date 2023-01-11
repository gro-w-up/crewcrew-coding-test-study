def solution(n, lost, reserve):
    '''
    여벌 체육복을 가져온 학생이 도난당했을 경우를 제외한다.
    진짜로 체육복을 잃어버리고, 빌려줄 수 있는 학생을 구한다.
    '''
    reverse_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for val in reverse_set:
        if val - 1 in lost_set:
            lost_set.remove(val - 1)
        elif val + 1 in lost_set:
            lost_set.remove(val + 1)

    return n - len(lost_set)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))