def solution(name):

    print('------------')

    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for idx, char in enumerate(name):
        # 해당 알파벳 변경 최소 이동 값 추가
        # print('전달받은 문자 : {}, A부터 시작: {}, Z부터 시작: {}'.format(char, ord(char) - ord('A'), ord('Z') - ord(char) + 1))
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음 문자의 마지막 A를 확인함.
        after = idx + 1
        while after < len(name) and name[after] == 'A':
            after += 1

        # 참고링크 : https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
        # 연속된 A의 -> 방식,
        # 연속된 A의 <- 방식
        print('idx : {}, len(name) : {}, name[idx] = {}, after : {}, 기존 : {}, -> : {}, <- : {}'
              .format(idx, len(name), name[idx], after, min_move, 2 * idx + len(name) - after, idx + 2 * (len(name) - after)))
        min_move = min(min_move, (2 * idx) + (len(name) - after), idx + (2 * (len(name) - after)))

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move

    return answer

# expect 56
print(solution("JEROEN"))
# expect 23
print(solution("JAN"))
# expect 14
print(solution("BCAAABCD"))

"""
    문제 풀이 및 접근 방법
        - 문제 단순화
            전달 받은 Name 파라미터 길이에 맞게 A로 초기화 되어있음
            ex. test -> 4 -> AAAA
"""

"""
B C A A A B C D
0 1 2 3 4 5 6 7
  '
  
"""