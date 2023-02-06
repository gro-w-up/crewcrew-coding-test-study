INF = 40000000  # n은 최대 200, 요금 최대 100000


def floyd(dist, n):
    for k in range(n):  # 경유지 노드 인덱스
        for i in range(n):  # 출발지
            for j in range(n):  # 도착지
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


def solution(n, s, a, b, fares):
    dist = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for edge in fares:
        dist[edge[0] - 1][edge[1] - 1] = edge[2]  # 문제에서는 1부터 쓰기 위해서 -1
        dist[edge[1] - 1][edge[0] - 1] = edge[2]  # 반대로도 갈 수 있기때문에

    floyd(dist, n)

    # 최단 비용 가지고 완전 탐색 시작
    # 인덱스는 1 시작이라 -1 해준다

    s -= 1
    a -= 1
    b -= 1
    answer = INF
    for k in range(n): # k 는 경유지
        answer = min(answer,dist[s][k] + dist[k][a]+ dist[k][b])