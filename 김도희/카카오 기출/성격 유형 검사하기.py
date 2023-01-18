def solution(survey, choices):
    response = {val: 0 for val in "RTCFJMAN"}
    neo_score = {i: 4-i for i in range(1, 4)}
    apeach_score = {4+i: i for i in range(1, 4)}

    answer = ''

    for idx, result in enumerate(survey):
        reply = choices[idx]

        if reply in neo_score:
            response[result[0]] += neo_score[reply]
        elif reply in apeach_score:
            response[result[1]] += apeach_score[reply]

    print(response)

    for category1, category2 in ["RT", "CF", "JM", "AN"]:
        if response[category1] > response[category2]:
            answer += category1
        elif response[category1] < response[category2]:
            answer += category2
        else:
            answer += chr(min(ord(category1), ord(category2)))

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
print(solution(["TR", "RT", "TR"], [4, 4, 4]))