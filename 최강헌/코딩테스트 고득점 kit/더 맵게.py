'''
풀이 및 접근방법
1. 최소 힙을 통하여 삽입 후 정렬
2. 힙에서 꺼낸 index > k 이면  섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
3.
'''
import heapq


def solution(scoville, K):
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    cnt = 0
    while heap:
        minValue = heapq.heappop(heap)
        if minValue < K:
            if not heap:
                return -1

            minSecondValue = heapq.heappop(heap)
            heapq.heappush(heap, minValue + (minSecondValue * 2))
            cnt += 1

    return cnt


# print('result 1 : ', solution([1, 2, 3, 9, 10, 12], 7))
print('result 2 : ', solution([1, 1, 1, 1, 1, 1], 50))
