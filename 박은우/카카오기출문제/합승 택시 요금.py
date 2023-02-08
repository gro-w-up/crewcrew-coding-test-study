import heapq

# n - 지점의개수, s : 출발지, a,b : 각각의 도착지, fares:간선정보
def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for i in fares:
        start, end, dist = i[0], i[1], i[2]
        graph[start].append((end, dist))
        graph[end].append((start, dist))

    INF = int(1e9)
    dist_list = [0]


    for i in range(1,n+1):
        distance = [INF] * (n + 1)
        dist_list.append(dijkstra(i, graph, distance))

    answer = INF
    for i in range(1,n+1):
        # s-i, i-a, i-b
        answer = min(answer, dist_list[s][i] + dist_list[i][a] + dist_list[i][b])
    return answer


def dijkstra(start, graph, distance):
    q = []

    # 힙에는 ( 거리, 노드) 튜플형식으로 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        curr = heapq.heappop(q)
        node = curr[1]
        dist = curr[0]
        if distance[node] < dist:  # 이미 처리된것
            continue

        # 현재노드와 연결된 노드에 대해서
        # 최단거리테이블에서 연결노드의값 : 현재노드~연결노드 + 현재노드의 최단거리테이블값
        for i in graph[node]:
            next_node = i[0]
            d = i[1]
            if distance[next_node] > dist + d:
                distance[next_node] = dist + d
                heapq.heappush(q, (dist + d, next_node))

    return distance


# Expect 82
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
# Expect 14
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# Expect 18
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))

"""
문제 유형 : 최단경로 구하기 (다익스트라, 플로이드워셜)

문제 풀이 및 접근 방법
1. 중간지점을 k (1<= k <= n) 이라고할때, 출발지~중간지점 + 중간지점~A + 중간지점~B 의 비용중 최소를 구해야하는 문제
2. 즉, 모든노드에서 모든노드까지의 최단경로를 알아야하므로 나는 출발지를 모든노드로 해서 다익스트라를 총 n번 호출해서 각각의 노드를 출발점으로해서 최단경로를 answer배열에 저장하였다.
3. 최단경로 테이블에서 현재 거리가 가장 작은 노드를 선택하는 과정에서 그냥 리스트로 풀었는데 이부분을 우선순위큐로 해결하면 시간복잡도를 로그엔까지 줄일수 있다. 
4. 우선순위큐로도 다시 풀어볼것 -> 우선순위큐를 이용해서 풀면 방문처리를 위한 visited배열이 필요없다!

"""