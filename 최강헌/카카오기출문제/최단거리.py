from collections import deque
def solution(maps):
    # 5x5 배열을 만들어준다
    n = len(maps); m = len(maps[0])
    #5x5 배열 방문여부를 표시한다
    visited = [[False]*m for _ in range(n)]
    #bfs 같은 경우 큐를 이용하여 풀면되며 dfs 같은경우 stack || 재귀
    q = deque()
    #처음 시작 0,0 을 넣어주고
    q.append((0, 0))
    #좌 우
    dx = [-1, 1, 0, 0]
    #상 하
    dy = [0, 0, -1, 1]
    #처음 시작은 방문처리를 해준다.
    visited[0][0]=True
    #queue 가 존재하면 계속 실행되며
    while q:
        #
        y, x = q.popleft()
        #움직임은 상 하 좌 우 이여서, 4번 반복
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    #거리 수를 더해준다.
                    maps[ny][nx] = maps[y][x]+1
    if maps[n-1][m-1]==1:
        return -1
    else:
        return maps[n-1][m-1]

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])