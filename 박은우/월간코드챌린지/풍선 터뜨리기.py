'''
- 접근 방법
    - 배열의 어떤 수든 자신의 왼쪽이나 오른쪽 방향에 자기보다 큰 수만 존재 할 시, 마지막까지 남기는 것이 가능합니다.
- 구현 포인트
    - for문 안에서 배열에서 앞의 값(왼쪽)과 뒤의 값(오른쪽)의 값을 각각 검사를 진행한다.
    - 한쪽 방향에서 자신이 가장 작을 시, 정답을 담는 result 배열에 True를 담습니다.
'''

def solution(a):
    answer = 2

    if 0 <= len(a) <= 2:
        return len(a)

    left, right = a[0], a[-1]
    print('left = {}, right = {}'.format(left, right))

    for i in range(1, len(a) - 1):
        print('i = {}, a[i] = {}, a[-1 - i] = {}, left = {}, right = {}, answer = {}'
              .format(i, a[i], a[-1 - i], left, right, answer))
        if left > a[i]:
            answer += 1
            left = a[i]
        if right > a[-1 - i]:
            answer += 1
            right = a[-1 - i]

    return answer if left != right else answer - 1

print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))