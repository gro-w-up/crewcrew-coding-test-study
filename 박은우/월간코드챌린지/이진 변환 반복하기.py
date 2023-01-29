def solution(s):
    answer = []

    # 이진 변환 횟수
    cnt_binary = 0
    # 각 회차별 s의 존재하는 0의 개수
    cnt_zero = 0

    while 1:
        # 종료 조건
        if s == "1":
            break

        # 종료 조건이 아닌 경우 이진 변환 횟수 증가
        cnt_binary += 1

        # 0의 개수 증가
        cnt_zero += s.count('0')

        # 0 -> ''
        s = s.replace('0', '')

        # s에 존재하는 1의 개수가 len임. 
        len_s = len(s)

        # len_s를 2진수로 변환 후 while문 반복 수행
        s = bin(len_s)[2:]

        # 디버그
        print('cnt_binary = {}, cnt_zero = {}, s = {}, len_s = {}, bin(len_s) = {}'.format(cnt_binary, cnt_zero, s, len_s, bin(len_s)))

    # 답안지 세팅
    answer.append(cnt_binary)
    answer.append(cnt_zero)

    return answer


s = "110010101001"
print(solution(s)) # Expect : [3, 8]
s = "110010101001"
print(solution(s)) # Expect : [3, 3]
s = "01110"
print(solution(s)) # Expect : [4, 1]