'''
풀이 및 접근방법
  1. 0,0위치부터 시작하므로 deque에 [0,0,1]을 세팅한다.
  2. place가 모두 비거나 목적지에 도달할때까지 다음을 반복한다.
   2-1. place의 선출되는 값을 y, x, i에 할당한다.
   2-2. y와 x좌표가 maps의 끝에 도달하면 i를 리턴하고 반복문을 멈춘다.
   2-3. y,x좌표에 0이 있으면 생략한다.
   2-4. 아니라면, y,x좌표를 이미 방문했으므로 다시 갈 수 없도록 0을 할당한다.
   2-5. y좌표기준으로 위 아래, x좌표 기준으로 왼쪽 오른쪽을 이동한 값을 place에 append한다.
'''

from collections import deque

def solution(maps):
  answer = -1
  place = deque([[0, 0, 1]])
  xLen = len(maps[0]) - 1
  yLen = len(maps) - 1
  while len(place):
    y, x, i = place.popleft()
    
    if y == yLen and x == xLen:
      answer = i
      break

    if maps[y][x] == 0:
      continue
    maps[y][x] = 0

    if y + 1 < len(maps):
      place.append([y + 1, x, i + 1])
    if x + 1 < len(maps[0]):
      place.append([y, x + 1, i + 1])
    if y - 1 >= 0:
      place.append([y - 1, x, i + 1])
    if x - 1 >= 0:
      place.append([y, x - 1, i + 1])
  return answer
