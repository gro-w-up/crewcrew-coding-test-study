def solution(n):
    answer = []
    array = [[0] * n for _ in range(n)]
    # print('초기화 array = {}'.format(array))
    x, y = -1, 0  # 처음엔 무조건 아래
    num = 1

    for i in range(n):  # 방향 check
        for _ in range(i, n):
            if i % 3 == 0:  # 아래
                x += 1
            elif i % 3 == 1:  # 오른쪽
                y += 1
            elif i % 3 == 2:  # 위쪽 대각선
                x -= 1
                y -= 1
            array[x][y] = num
            num += 1
            # print('i = {}, x = {}, y = {}, array[x][y] = {}, num = {}'.format(i, x, y, array[x][y], num))

    # print('처리 완료 array = {}'.format(array))
    for i in array:
        for j in i:
            if j > 0:
                # print('j = {}'.format(j))
                answer.append(j)
    return answer

print(solution(4))
print(solution(5))
print(solution(6))

"""
문제풀이 및 접근법
- 삼각 달팽이 지만.. 사각형으로 생각하자
- 
"""