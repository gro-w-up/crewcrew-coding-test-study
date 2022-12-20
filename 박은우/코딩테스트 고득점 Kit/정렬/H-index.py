# def solution(citations):
#     answer = 0
#
#     citations.sort()
#     print(citations)
#     n = len(citations)
#
#     for index in range(n):
#
#         h_index = n - index
#
#         print('n : ', n, ', citaions[index] : ', citations[index], ', index : ', index, ', h-index : ', h_index)
#
#         # 순회하는 배열에서 h_index와 크거나 같은지 확인한다.
#         # 정렬한 배열에서 찾기 때문에 항상 가장 작은 h_index만 만족한다.
#         if citations[index] >= h_index:
#             answer = h_index
#             break
#
#     return answer
def solution(citations):
    sorted_citations = sorted(citations, reverse=True)
    for i in range(len(sorted_citations)):
        print('sorted_citations =', sorted_citations, ', sorted_citations[i] : ', sorted_citations[i], ', i =', i)
        if sorted_citations[i] <= i:
            return i
    return len(sorted_citations)

print(solution([3, 0, 6, 1, 5]))
print(solution([4, 1, 7, 2, 6]))
print(solution([5, 2, 8, 4, 8]))
"""
접근 및 풀이 방법
    - 문제 단순화
        1. H-index는 N편 중 h번 이상, h번 이하 인용된 수를 뜻한다.
        2. N : citations의 사이즈
    - 접근 방법
        H-index 개념 정리
        디버그 표 작성
    - 참고자료 (위키)
        h-지수는 h개의 기사가 각각 h개 이상의 인용을 가질 수 있는 가장 큰 숫자 h입니다.
        예를 들어 인용문이 9, 7, 6, 2, 1개(가장 큰 것부터 가장 작은 것까지)인 5개의 출판물이 있는 경우, 
        인용문이 3개 이상인 출판물이 3개 있기 때문에 저자의 h-index는 3이 됩니다.
        그러나 저자는 인용이 4개 이상인 출판물을 4개 가지고 있지 않다.
        
"""
"""
디버그
[3, 0, 6, 1, 5]
n = 5
n | value | >= | <= | Y/N
--------------------------
0 |     0 |  5 |  1 | N
1 |     1 |  4 |  2 | N
2 |     3 |  4 |  2 | N
3 |     5 |  3 |  3 | Y
4 |     6 |  2 |  3 | N
h-index = 3

[4, 1, 7, 2, 6]
n = 5
n | value | >= | <= | Y/N
--------------------------
0 |     1 |  5 |  0 | N
1 |     2 |  5 |  1 | N
2 |     4 |  4 |  2 | N
3 |     6 |  3 |  2 | Y
4 |     7 |  3 |  3 | Y
h-index = 3

[5, 2, 8, 4, 8]
n = 5
n | value | >= | <= : Y/N
------------------
0 |     2 |  5 |  0 | N
1 |     4 |  5 |  0 | N
2 |     5 |  5 |  1 | N
3 |     8 |  4 |  1 | N
4 |     8 |  4 |  2 | Y
"""