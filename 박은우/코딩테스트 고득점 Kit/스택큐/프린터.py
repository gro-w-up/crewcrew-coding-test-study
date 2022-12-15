def solution(priorities, location):

    # A, B, C, D -> 0, 1, 2, 3
    index_list = []
    for index in range(len(priorities)):
        index_list.append(index)

    priorities_list = priorities.copy()

    i = 0
    while True:
        if priorities_list[i] < max(priorities_list[i+1:]):
            index_list.append(index_list.pop(i))
            priorities_list.append(priorities_list.pop(i))
        else:
            i += 1

        if priorities_list == sorted(priorities, reverse=True):
            break;


    return index_list.index(location) + 1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

"""
접근 및 풀이 방법
    문제 단순화
        - 중요도가 높은 문서를 먼저 인쇄하는 프린터
        - 중요도가 담겨있는 배열 : priorities 
        - 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지 : location
    풀이 계획
        - 문서를 의미하는 A, B, C, D를 수치로 표현할 수 있는 위치 저장 배열 생성
        - 현재 index의 Value값이 해당 리스트에 맥스값보다 작은 경우에 뒤에 붙힐 수 있도록 Queue자료 구조 사용
        - 이 때, 문서의 위치 배열도 같이 처리해서 항상 같은 index와 Value값을 가질 수 있도록 작성
        - priorities 배열을 내림차순을 한 것과 처리한 Value 리스트의 값이 같은 경우에 리스트 처리를 중지
        - index배열에서 위치값 출력 후 반환
"""

"""
다른 사람의 풀이

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
"""