def solution(n, lost, reserve):
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)

    for i in reserve_only:
        f = i - 1
        b = i + 1

        if f in lost_only:
            lost_only.remove(f)
        elif b in lost_only:
            lost_only.remove(b)

    return n - len(lost_only)
'''
1차 풀이
def solution(n, lost, reserve):
    for i in reserve:
        if lost in reserve:
            lost.remove(i)
            reserve.remove(i)

    for j in reserve:
        if j in lost:
            lost.remove(j)
        elif j - 1 in lost:
            lost.remove(j - 1)
        elif j + 1 in lost:
            lost.remove(j + 1)

    return n - len(lost)

'''
# expect 5
print(solution(5, [2, 4], [1, 3, 5]))
# expect 4
print(solution(5, [2, 4], [3]))
# expect 2
print(solution(3, [3], [1]))
