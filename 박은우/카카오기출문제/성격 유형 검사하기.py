def solution(survey, choices):
    answer = ''

    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for s, c in zip(survey, choices):
        if c > 4: dic[s[1]] += c - 4
        if c < 4: dic[s[0]] += 4 - c
        print('s = {}, c = {}, dic = {}'.format(s, c, dic))

    li = list(dic.items())

    print('li = {}'.format(li))
    for i in range(0, 8, 2):
        print('li[i][0] = {}, li[i][1] = {}, li[i+1][0] = {}, li[i+1][1] = {}'.format(li[i][0], li[i][1], li[i+1][0], li[i+1][1]))
        if li[i][1] < li[i + 1][1]:
            answer += li[i + 1][0]
        else:
            answer += li[i][0]

    return answer

# def solution(설문_조사_배열, 선택지_배열):
#     성격_유형 = ''
#
#     점수_표 = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
#
#     for 설문, 선택지 in zip(설문_조사_배열, 선택지_배열):
#         if 선택지 > 4: 점수_표[설문[1]] += 선택지 - 4
#         if 선택지 < 4: 점수_표[설문[0]] += 4 - 선택지
#
#     점수_표_리스트 = list(점수_표.items())
#
#     for 인덱스 in range(0, 8, 2):
#         if 점수_표_리스트[인덱스][1] < 점수_표_리스트[인덱스+1][1]:
#             성격_유형 += 점수_표_리스트[인덱스+1][0]
#         else:
#             성격_유형 += 점수_표_리스트[인덱스][0]
#
#     return 성격_유형

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))