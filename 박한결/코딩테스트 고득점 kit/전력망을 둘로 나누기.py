'''
풀이 및 접근방법

  1) 메인로직
    1. 일단 로직을 구현하기 위해 다음과 같이 기본값을 세팅한다.
      1-1. bfs로 값을 구하기 위해 n의 갯수만큼 False를 넣어 visited를 세팅한다.
      1-2. 각 송전탑마다 연결된 선을 구하기 위해 1부터 n까지의 key를 갖는 딕셔너리 dict를 세팅한다.
    2. 다음의 과정을 wires를 순회하며 반복한다.
      2-1. 리스트 arr에 wires를 복제해 세팅한다.
      2-2. 딕셔너리 dict2에 dict를 깊은복사해 세팅한다.
      2-3. 끊어진 전선을 arr에서 삭제한다.
      2-4. 각 송전탑마다 연결된 선을 구해서 dict2에 세팅한다.
      2-5. 리스트 graph를 세팅하고, 거기에 dict2의 밸류값들을 추가한다.
      2-6. 세팅한 graph를 이용해 bfs 함수를 작동해, true가 반환된 갯수들을 ans에 세팅한다.
    3. ans를 순회하며 n을 2로 나눈 값과의 차이를 재할당한다.
    4. 송전탑 개수가 가장 비슷할 때의 수를 ans의 최소값을 통해 구한다.
    5. 두 전력망의 차이를 리턴한다.
'''

from collections import deque
import copy
import math

def bfs(graph, start, visited):
  queue = deque([start])
  visitedCopy = visited.copy()
  visitedCopy[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visitedCopy[i]:
        queue.append(i)
        visitedCopy[i] = True
  return visitedCopy


def solution(n, wires):
  visited = [False] * (n + 1)
  dict = {}
  ans = []
  for i in range(1, n + 1):
    dict[i] = []
  for index, el in enumerate(wires):
    arr = wires.copy()
    dict2 = copy.deepcopy(dict)
    del arr[index]
    for e1, e2 in arr:
      dict2[e1].append(e2)
      dict2[e2].append(e1)
    graph = [[]]
    for i in dict2:
      graph.append(dict2[i])
    ret = bfs(graph, 1, visited)
    ans.append(ret.count(True))
  for index, e in enumerate(ans):
    ans[index] = abs(n/2 - e)
  ans1 = min(ans) + n/2
  ans2 = n - ans1
  return math.ceil(abs(ans1 - ans2))
