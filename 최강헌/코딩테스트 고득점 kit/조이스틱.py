from re import A


def solution(name):
    # 상하 조정으로 알파벳 바꾸기
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    charA = 'A'  # 로그용
    charZ = 'Z'  # 로그용
    for i in name:
        # 문자 별로 상하로 움직여 최단 거리를 계산한다.
        print(f'min(ord(i) - ord(A) = {ord(i) - ord(charA)} min(ord(Z) - ord(i) = {ord(charZ) - ord(i) + 1}')
    idx = 0
    answer = 0

    print(change)
    while True:
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0:
            return answer

        # 좌우 이동향방을 정하기
        # 좌우측으로 계속 가다가 먼저 0 이나면 멈춘다.
        # 그 이유는 좌우로 그나마 덜 가기 위해서
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        # 위치(인덱스) 조정

        ''' 이것은 예전 풀이이며, 현재는 테스트케이스가 추가하여 사용하지못함
        이해하기 편해서 작성해둠
        if left >= right:
            idx += right
            answer += right

        else:
            idx -= left
            answer += left
        '''

print(solution("JEROEN"))
# expect 23
print(solution("JAN"))
# expect 14
print(solution("BCAAABCD"))
