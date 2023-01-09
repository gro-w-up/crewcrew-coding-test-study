from collections import deque

dx = [-1, 1, 0, 0] # 상하
dy = [0, 0, -1, 1] # 좌우

def bfs(maps, x, y):
    global n, m
    queue = deque()
    queue.append((x, y)) # 초기화 0, 0


    cnt = 0
    while queue:
        cnt += 1
        print('cnt = {}'.format(cnt), end='')
        print(' queue = {}'.format(queue))
        x, y = queue.popleft();
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            print('nx = {}, ny = {}'.format(nx, ny));

            # 게임 맵을 벗어난 길은 갈 수 없음
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽이 있는 자리
            if maps[nx][ny] == 0:
                continue

            # 지나갈 수 있는 자리
            if maps[nx][ny] == 1:
                # 지나간 칸 수 계산
                maps[nx][ny] = maps[x][y] + 1
                print('maps[nx][ny] = {}'.format(maps[nx][ny]))
                queue.append((nx, ny))

    return maps[n -1][m - 1]

def solution(maps):

    print('---------------')
    global n
    global m

    n = len(maps)
    m = len(maps[0])

    print('n = {}, m = {}'.format(n, m));

    answer = bfs(maps, 0, 0)

    if answer == 1:
        answer = -1

    return answer


# expect 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
# expect -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

"""
문제 접근 및 풀이 방법
    - 상대 팀 진영에 최대한 빨리 도착해서 먼저 파괴하면 이기는 게임.
    - 1,1(캐릭터) 5,5(상대팀)
    - n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
    - 0은 벽이 있는 자리, 1은 벽이 없는 자리
    - 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 
    - 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.
"""

"""
1, 0, 1, 1, 1           V, 0, 1, 1, 1 
1, 0, 1, 0, 1           V, 0, 1, 0, 1 
1, 0, 1, 1, 1    ->     V, 0, V, V, V   -> 11
1, 1, 1, 0, 1           V, V, V, 0, V 
0, 0, 0, 0, 1           0, 0, 0, 0, V 
"""

"""
1, 0, 1, 1, 1           #, 0, 1, 1, 1 
1, 0, 1, 0, 1           1, 0, 1, 0, 1 
1, 0, 1, 1, 1    ->     1, 0, 1, 1, 1    -> 도달 할 수 없음 -1 
1, 1, 1, 0, 0           1, 1, 1, 0, 0 
0, 0, 0, 0, 1           0, 0, 0, 0, @ 
"""