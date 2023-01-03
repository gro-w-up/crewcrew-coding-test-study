def solution(info, query):

    answer = []
    for q in query:
        print('-------')
        q = q.replace("and ", "")
        q = q.split()
        print(' q = {}'.format(q))
        count = 0
        for i in info:
            i = i.split()
            print(' i = {}'.format(i))
            flag = True
            if int(i[4]) < int(q[4]):
                flag = False
            else:
                for idx in range(4):
                    print('q[idx] = {}, i[idex] = {}'.format(q[idx], i[idx]))
                    if q[idx] == "-":
                        continue
                    else:
                        if q[idx] != i[idx]:
                            flag = False
                            break
            if flag:
                count += 1
        answer.append(count)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
"""

파싱
query의 "and "를 제거 후 공백을 기준으로 나누기
info 또한 공백을 기준으로 나누기

비교
반복문으로 단순 비교하는 방식
우선 점수를 비교하여 작다면 다른 조건을 보지 않는다.
query의 조건이 "-"가 아니라면 비교하게 된다,
두 값이 같지 않다면 flag는 False가 되고 반복문을 빠져나온다.
flag의 True, False 여부로 count를 증가시킨 후 해당 count값을 결과 answer 리스트에 추가하는 식으로 구현

언어	직군	경력	소울 푸드	점수
java	backend	junior	pizza	150
python	frontend	senior	chicken	210
python	frontend	senior	chicken	150
cpp	backend	senior	pizza	260
java	backend	junior	chicken	80
python	backend	senior	chicken	50


"java and backend and junior and pizza 100" : 
java로 코딩테스트를 봤으며, backend 직군을 선택했고 junior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 100점 이상 받은 지원자는 1명 입니다.

"python and frontend and senior and chicken 200" : 
python으로 코딩테스트를 봤으며, frontend 직군을 선택했고, senior 경력이면서 소울 푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 200점 이상 받은 지원자는 1명 입니다.

"cpp and - and senior and pizza 250" : 
cpp로 코딩테스트를 봤으며, senior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 250점 이상 받은 지원자는 1명 입니다.

"- and backend and senior and - 150" : 
backend 직군을 선택했고, senior 경력인 지원자 중 코딩테스트 점수를 150점 이상 받은 지원자는 1명 입니다.

"- and - and - and chicken 100" : 
소울푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 100점 이상을 받은 지원자는 2명 입니다.

"- and - and - and - 150" : 
코딩테스트 점수를 150점 이상 받은 지원자는 4명 입니다.
"""