from collections import defaultdict


def solution(clothes):
    # [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    # ->
    # {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}

    answer = 1
    closet = defaultdict(list)

    for item, category in clothes:
        closet[category].append(item)

    for item, category in closet.items():
        answer *= len(category) + 1
        print(item, category, 'answer : ', answer)

    return answer -1

# 테스트 케이스
print('예제 1 : ', solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print('예제 2 : ', solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))