def solution(clothes):
    return len(".".join(clothes))-1

# 테스트 케이스
print('예제 1 : ', solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print('예제 2 : ', solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))