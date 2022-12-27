cnt = 0
# https://it-jm.tistory.com/179
def DFS(v, ch, graph):
    global cnt
    ch[v] = 1
    cnt += 1
    for i in graph[v]:
        if ch[i] == 0:
            DFS(i, ch, graph)


def solution(n, wires):
    global cnt
    answer = n
    graph = [[] for _ in range(n + 1)]
    cnt = [0] * (n - 1)

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:
        ch = [0] * (n + 1)
        # 끊는 역할
        ch[v2] = 1
        cnt = 0
        DFS(v1, ch, graph)
        answer = min(answer, abs(cnt - (n - cnt)))
        print(answer)
    return answer


solution(9,	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])