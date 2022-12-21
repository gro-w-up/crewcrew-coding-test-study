from heapq import heappush, heappop


def solution(scoville, K):
    answer = 0
    scoville_heap = []

    for scov in scoville:
        heappush(scoville_heap, scov)

    while len(scoville_heap) >= 2:
        answer += 1
        targets = []

        for _ in range(2):
            targets.append((heappop(scoville_heap)))

        heappush(scoville_heap, targets[0] + (targets[1] * 2))

        lowest = heappop(scoville_heap)

        if lowest >= K:
            return answer
        else:
            heappush(scoville_heap, lowest)

    return -1