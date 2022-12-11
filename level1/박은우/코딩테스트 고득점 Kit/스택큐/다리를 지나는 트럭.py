def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for _ in range(bridge_length)]

    while bridge:
        # print('time : ', time, ", bridge : ", bridge)
        time += 1
        # Note. 효율성 많이 떨어짐 pop하고 나서 뒤에 있는 자료들 한칸씩 앞으로 가져오기 때문
        bridge.pop(0)

        if truck_weights:
            # Note. 마찬가지 첫 인덱스부터 마지막인덱스까지 모두 돌면서 더하기 때문임
            if sum(bridge) + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
            else:
                bridge.append(0)

    return time

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))

"""
접근 및 풀이 방법
    문제 단순화
        - 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 함
            - 다리에 올라갈 수 있는 트럭 수 : bridge_length
            - 다리가 견딜 수 있는 무게 : weight 
            - 트럭 별 무게 : truck_weights
        - 다리에 완전히 오르지 않은 트럭의 무게는 무시
    풀이 계획
        - 올라갈 수 있는 트럭의 수를 담을 수 있는 빈 배열 생성
        - 첫번째 자리 부터 처리하기 위해 Queue 자료 구조 사용
        - 트럭별 무게와 현재 다리에 올라간 트럭의 합이 다리가 견딜 수 있는 무게 보다 작거나 같은 경우에 다리에 트럭 적재
            - 위의 조건이 아닌 경우에는 초기값 '0' 세팅
        - 적재된 트럭은 대기 목록에서 제외
"""

"""
채점 결과
테스트 01 〉통과 (11.34ms, 10.2MB)
테스트 02 〉통과 (1508.29ms, 10.1MB)
테스트 03 〉통과 (0.02ms, 10.1MB)
테스트 04 〉통과 (314.56ms, 10MB)
테스트 05 〉통과 (9859.30ms, 10.3MB)
테스트 06 〉통과 (1583.71ms, 10.2MB)
테스트 07 〉통과 (5.75ms, 10.1MB)
테스트 08 〉통과 (0.31ms, 10.2MB)
테스트 09 〉통과 (5.39ms, 10.2MB)
테스트 10 〉통과 (0.25ms, 10.2MB)
테스트 11 〉통과 (0.01ms, 10.3MB)
테스트 12 〉통과 (0.26ms, 10.1MB)
테스트 13 〉통과 (3.43ms, 10.2MB)
테스트 14 〉통과 (0.02ms, 10.2MB)
"""