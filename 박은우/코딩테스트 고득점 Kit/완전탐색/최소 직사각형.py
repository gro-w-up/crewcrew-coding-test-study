def solution(sizes):

    for x in sizes:
        print(x, ', max : ', max(x), ', min : ', min(x))

    width = max((max(x) for x in sizes))
    height = max((min(x) for x in sizes))

    return width * height

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

"""
접근 및 풀이 방법
    - 문제 단순화
        1. 가로 * 세로 크기의 지갑을 만들 때 모두 수납 가능한 가장 작은 사이즈
    - 접근 방법
        1. 가장 큰 가로와 가장 큰 세로를 구해야한다.
        2. 단, 회전 시켜도 동일해야 한다.
"""
