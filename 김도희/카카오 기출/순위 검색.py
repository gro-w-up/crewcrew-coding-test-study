from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    conditions = defaultdict(list)
    index = list(range(4))
    # 모든 조건 : 점수

    for inf in info:
        now = inf.split()
        score = int(now.pop())

        for i in range(5):
            for case in combinations(index, i):
                temp = now.copy()
                for idx in case:
                    temp[idx] = "-"
                key = ''.join(temp)
                conditions[key].append(score)
        #현재 대상이 조건으로 검출될 수 있는 모든 가능성을 체크한다

    for value in conditions.values():
        value.sort()

    for q in query:
        q = q.replace("and ", "")
        q = q.split()

        target_score = int(q.pop())
        target_key = ''.join(q)
        count = 0

        if target_key in conditions:
            target_candidate = conditions[target_key]
            idx = bisect_left(target_candidate, target_score)

            count = len(target_candidate) - idx

        answer.append(count)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))