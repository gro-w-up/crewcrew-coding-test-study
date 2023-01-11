def solution(msg):
    print('--------------')
    answer = []

    # Step 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    # 딕셔너리 선언
    dictionary = {chr(e + 64): e for e in range(1, 27)}

    # dictionary = dict()
    #
    # for char in range(ord('A'), ord('Z') + 1): #65~91
    #     # print('c = {}, ord(c) = {}'.format(chr(c), c))
    #     dictionary[chr(char)] = (char - ord('A')) + 1
    idx = 27
    start, end = 0, 1

    # 길이 만큼 반복한다.
    while end < len(msg) + 1:
        # msg데이터에서 한글자씩 처리하기 위한 슬라이싱
        char = msg[start:end]

        # 현재 문자가 딕셔너리에 있나?
        if char in dictionary:
            # 다음문자까지 처리
            end += 1
        else:

            print('dictionary[char] = {}, char = {}, index = {}'.format(dictionary[char[:-1]], char, idx))
            # 현재 입력 + 다음 글자 기준에서 다음글자를 뺀 문자의 색인번호 추가
            answer.append(dictionary[char[:-1]])
            # 사전 추가 [KA]
            dictionary[char] = idx
            # 색인번호 증가
            idx += 1
            # 다음 문자를 처리하기 위해 start 변경
            start = end - 1
    # 사전에 있는 경우에는 색인번호 추가
    answer.append(dictionary[char])

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))

"""
LZW 압축
1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다.
"""
"""
압축 알고리즘이 영문 대문자만 처리한다고 할 때, 사전은 다음과 같이 초기화된다. 사전의 색인 번호는 정수값으로 주어지며, 1부터 시작한다고 하자.

색인 번호	1	2	3	...	24	25	26
단어	A	B	C	...	X
"""
"""
예를 들어 입력으로 KAKAO가 들어온다고 하자.

현재 사전에는 KAKAO의 첫 글자 K는 등록되어 있으나, 두 번째 글자까지인 KA는 없으므로, 첫 글자 K에 해당하는 색인 번호 11을 출력하고, 다음 글자인 A를 포함한 KA를 사전에 27 번째로 등록한다.
두 번째 글자 A는 사전에 있으나, 세 번째 글자까지인 AK는 사전에 없으므로, A의 색인 번호 1을 출력하고, AK를 사전에 28 번째로 등록한다.
세 번째 글자에서 시작하는 KA가 사전에 있으므로, KA에 해당하는 색인 번호 27을 출력하고, 다음 글자 O를 포함한 KAO를 29 번째로 등록한다.
마지막으로 처리되지 않은 글자 O에 해당하는 색인 번호 15를 출력한다.
현재 입력(w)	다음 글자(c)	출력	사전 추가(w+c)
K	A	11	27: KA
A	K	1	28: AK
KA	O	27	29: KAO
O		15	
"""