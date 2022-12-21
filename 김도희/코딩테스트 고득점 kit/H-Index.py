from bisect import bisect_left

def solution(citations):
    answer = 0
    citations.sort()
    start, end = citations[0], citations[-1]
    length = len(citations)

    for h_index in range(end + 1):
        left = bisect_left(citations, h_index)
        right = length - left

        if left <= h_index <= right:
            answer = max(h_index, answer)

    return answer

print(solution([3, 0, 6, 1, 5]))