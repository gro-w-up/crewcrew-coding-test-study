# def solution(scoville, K):
#
#     mix_count = 0
#
#     while min(scoville) < K :
#         scoville.sort()
#         try:
#             scoville.append(scoville.pop(0) + (scoville.pop(0) * 2))
#         except IndexError:
#             return -1
#
#         mix_count += 1
#         print(mix_count, ':', scoville)
#
#     return mix_count

# heapq는 push, pop 할 때 마다, 자동으로 정렬해주는 자료구조임
# 위에서 코딩한 내용 중 정렬 비용을 감소 시켜 효율성 이슈를 해결 할 수 있음.
import heapq
def solution(scoville, K):

    mix_count = 0
    heap = []
    for value in scoville:
        heapq.heappush(heap, value)

    while heap[0] < K :
        # print(mix_count, ':', scoville)
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1

        mix_count += 1

    return mix_count

print(solution([1, 2, 3, 9, 10, 12], 7))

"""
접근 및 풀이 방법
    - 문제 단순화
        1. 모든 음식의 스코빌 지수가 K 이상 될 때 까지 반복
        2. 음식의 스코빌 지수를 담은 배열 scoville
        3. 원하는 스코빌 지수 K
        4. 수식 
        섞은 음식의 스코빌 지수 
            = 
            가장 맵지 않은 음식의 스코빌 지수 
            + 
            (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        5. 
    - 접근 방법
         섞은 횟수를 리턴할 변수 mix_count 선언
         작은 스코빌 지수 부터 오름차순으로 정렬한 배열 scoville_asc_array 선언
         가장 작은 스코빌 지수가 K보다 작을 때 마다 loop 돌림 (O(n))
         수식 계산해서 다시 scovile 리스트에 넣어준다.
         섞은 횟수 + 1
         
"""

"""
채점 결과
    채점을 시작합니다.
        정확성  테스트
        테스트 1 〉	통과 (0.01ms, 10.1MB)
        테스트 2 〉	통과 (0.00ms, 10.2MB)
        테스트 3 〉	통과 (0.01ms, 10.1MB)
        테스트 4 〉	통과 (0.01ms, 10.2MB)
        테스트 5 〉	통과 (0.01ms, 10.2MB)
        테스트 6 〉	통과 (0.42ms, 10.2MB)
        테스트 7 〉	통과 (0.36ms, 10.3MB)
        테스트 8 〉	통과 (0.05ms, 10.2MB)
        테스트 9 〉	통과 (0.04ms, 10.2MB)
        테스트 10 〉	통과 (0.30ms, 10.2MB)
        테스트 11 〉	통과 (0.19ms, 10.2MB)
        테스트 12 〉	통과 (0.69ms, 10.3MB)
        테스트 13 〉	통과 (0.36ms, 10.2MB)
        테스트 14 〉	통과 (0.01ms, 10.2MB)
        테스트 15 〉	통과 (0.47ms, 10.1MB)
        테스트 16 〉	통과 (0.00ms, 10.1MB)
        효율성  테스트
        테스트 1 〉	통과 (168.50ms, 18.8MB)
        테스트 2 〉	통과 (375.98ms, 27MB)
        테스트 3 〉	통과 (1523.92ms, 63.9MB)
        테스트 4 〉	통과 (141.26ms, 17.1MB)
        테스트 5 〉	통과 (1674.37ms, 71.3MB)
        채점 결과
        정확성: 76.2
        효율성: 23.8
        합계: 100.0 / 100.0
"""