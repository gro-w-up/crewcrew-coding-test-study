from itertools import combinations
from collections import deque
def solution(n, wires):
    # 간선을 -1개만 이용하여 조합 생성
    cases = list(combinations(wires, len(wires) - 1))
    print(cases)
    def bfs(x, arr):
        # 방문 처리 후 큐 생성
        visited[x] = True
        q = deque([x])
        # 연결된 탑의 수
        connected_num = 1

        # 큐가 빌 때까지
        while q:
            # 맨 먼저 들어온 원소를 꺼내어
            test = q.popleft()
            # 연결된 탑들을 확인
            for next in graph[test]:
                # 방문하지 않은 탑을 큐에 추가하고 방문 처리
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    connected_num += 1
        # 연결된 탑의 수를 반환
        return connected_num

    # 탑 개수 차이를 담을 리스트
    answer = []
    # 각 숫자 조합에 대해
    for case in cases:
        # 연결 그래프와 방문 리스트 초기화
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)

        # 무방향 그래프 생성
        for send in case:
            graph[send[0]].append(send[1])
            graph[send[1]].append(send[0])

        # 카운트를 담을 리스트 초기화
        cnt_list = []

        # 1번부터 n번 탑까지
        for i in range(1, n + 1):
            # 방문 전이라면 탐색 실행
            if not visited[i]:
                temp = bfs(i, cnt_list)
                # 연결된 탑의 수를 리스트에 추가
                cnt_list.append(temp)

        # 탑의 수 차이를 최종 리스트에 추가®
        answer.append(abs(cnt_list[0] - cnt_list[1]))

    # 탑의 수 차이가 가장 작은 것을 반환
    return min(answer)

# expect 3
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# expect 0
print(solution(4, [[1,2],[2,3],[3,4]]))
# expect 1
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
