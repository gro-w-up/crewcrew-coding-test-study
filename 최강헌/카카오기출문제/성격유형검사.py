from collections import defaultdict
# defaultdict를 쓰는 이유는 입력으로 survey에서 지표에 대한것이 안나올 수도 있음.
# 기본 점수 0 을 표현하기 위해서

def solution(survey, choices):
    score = defaultdict(int)
    for sv, choice in zip(survey, choices):
        # print(f"sv: {sv}, choice = {choice}")
        if choice > 4:  # 동의 관련된 성격 유형
            score[sv[1]] += choice - 4
        elif choice < 4: # 비동의에 대한 성격 유형
            score[sv[0]] += 4 - choice

    # print(f"score : {score}")

    answer = []
    indices_1 = "R" if score["R"] >= score["T"] else "T"
    indices_2 = "C" if score["C"] >= score["F"] else "F"
    indices_3 = "J" if score["J"] >= score["M"] else "M"
    indices_4 = "A" if score["A"] >= score["N"] else "N"

    answer = indices_1 + indices_2 + indices_3 + indices_4
    return  answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
solution(survey, choices)
