'''
1. 이모티콘 플러스를 최대한 늘리기
2. 이모티콘 플러스 가입자가 같다면 이모티콘 구매 비용이 높을수록 좋다.

<풀이>
1. 탐색
2. 탐색 시간 -> 어떻게 줄일 수 있을까?
 1) 이분 탐색, dp, greedy 같은 알고리즘
 2) 완전 탐색(0) -> 탐색 시간을 어떻게 해도 줄일 수 없는 경우 / 시간이 남아돌떄

3. 탐색 시간 계산
완전 탐색을 한다고 할떄 시간이 얼마나 걸리지?
-> 4가지 할인율 (10,20,30,40%)
-> 이모티콘은 최대 7개
-> 2** 14 (16,000정도)
-> 16000 * 100(유저길이)
* 시간 복잡도를 계산했을때 연산 횟수가 1억 회 이하면 사용가능한 알고리즘
'''
from itertools import product


def solution(users, emoticons):
    answer = [0,0] # 플러스 가입 수 , 이모티콘 매출액
    cases = [10, 20, 30, 40]

    for case in product(cases, repeat=len(emoticons)): #완전 탐색 (16,000)
        total_pay, plus_num = 0, 0
        for rate, price in users: # 만개
            pay = 0

            for i, emoticon in enumerate(emoticons): # 7개
                if case[i] >= rate: # 이모티콘 할인률(case[i]가 rate보다 크기 떄문에 이모티콘 구매
                    pay += emoticon * (100-case[i]) // 100
            if pay >= price: # 이모티콘 구매를 모두 취소하고 플러스 가입
                plus_num += 1
            else: # 이모티콘 플러스에 가입 하지 않는 경우
                total_pay += pay
        if plus_num > answer[0]: # 이모티콘 플러스 가입자 수가 증가한 경우
            answer[0], answer[1] = plus_num, total_pay
        elif plus_num == answer[0] and total_pay > answer[1]: # 플러스 가입자 수는 같으면서 매출액은 증가
            answer[1] = total_pay
    return answer

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
answer = solution(users, emoticons)
print(answer)
