'''
풀이 및 접근방법
  1. 배열로 초기화하기 위해, 각각의 지점 s, a, b에 1씩을 뺀다.
  2. 각각의 연결지점으로 된 fares를 순회하며, 각 지점에서 다른 지점과의 거리가 담긴 배열 graph를 세팅한다.
     이 때, 직접적으로 연결되지 않으면 거리를 inf로 세팅한다.
  3. 어느 지점에서 다른 지점으로 이동하는 최단 거리가 담긴 모든 배열을 min_graph에 담아야 한다.
     이를 위해, 모든 지점을 순회하며 다익스트라 알고리즘을 이용해 최단거리를 구한다.
  4. 모든 지점을 순회하며, s에서 해당 지점을 찍은 후 a, b로 각각 가는 거리의 합 중 최소값을 구해 리턴한다.

  다익스트라
  1. 자신에서 자신으로의 거리는 0, 나머지 지점과의 거리를 inf로 세팅해 dist에 저장한다.
  2. 시작지점과 거리를 heapq를 이용해 q에 세팅한다.
  3. heapq를 순회하며, 비용이 작은 노드를 먼저 선택한다.
  4. 만약 선택된 노드의 거리값이 dist에 저장된 거리값보다 작을 때에 다음을 진행한다.
  5. 해당 지점에서 다른 지점으로 가는 모든 거리값을 구해, 그 거리가 dist에 저장된 거리값보다 작으면 dist에 갱신한다.
  6. 다음 인접한 노드를 고려하기 위해 새로 구해진 거리값과 노드 인덱스를 q에 세팅한다.
'''


from math import inf
from heapq import heappush, heappop


def dijkstra(n, graph, start):
    dist = [inf for _ in range(n)]  # start 기준의 거리행렬
    dist[start] = 0                 # 자기 자신으로 가는 간선은 0
    q = []
    heappush(q, [dist[start], start])           # 거리와 노드를 함께 큐에 삽입
    while q:                                    # (비용이 작은 노드를 먼저 선택)
        cur_dist, cur_idx = heappop(q)
        if dist[cur_idx] >= cur_dist:          # start에서 cur_dest로 가는 거리가
            for i in range(n):                  # 이미 저장된 거리보다 작을 때만 진행
                new_dist = cur_dist + graph[cur_idx][i]
                if new_dist < dist[i]:          # cur_dest를 거쳐 i로 가는 거리가
                    dist[i] = new_dist          # 이미 저장된 거리보다 작으면 갱신
                    heappush(q, [new_dist, i])  # 다음 인접한 노드를 고려하기 위해 큐에 삽입
    return dist


def solution(n, s, a, b, fares):
    s, a, b = s - 1, a - 1, b - 1   # 0부터 시작하는 인덱스
    graph = [[inf] * n for _ in range(n)]
    for fare in fares:
        u, v, w = fare
        graph[u - 1][v - 1] = graph[v - 1][u - 1] = w
    # 다익스트라
    # 모든 노드에 대해 다익스트라를 수행하고,
    # 반환된 1차원 거리행렬을 append 해줌
    min_graph = []
    for i in range(n):
        min_graph.append(dijkstra(n, graph, i))
    # 출발점을 기준으로 어떤 지점 k를 거쳐 각각 a와 b로 가는 최소 비용을 탐색
    ans = inf
    for k in range(n):
        ans = min(ans, min_graph[s][k] + min_graph[k][a] + min_graph[k][b])

    return ans