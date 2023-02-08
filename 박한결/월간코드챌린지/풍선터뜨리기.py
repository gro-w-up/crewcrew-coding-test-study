'''
풀이 및 접근방법
  1. 해당 풍선이 살아남기 위해서는, 해당 풍선의 양옆의 최소값을 구한 다음, 그 최소값들보다 가장 크지 않아야 한다.
     (한 번만 작은 수를 터뜨릴 수 있기 때문에)
  2. 그렇기에 숫자마다 양 옆의 최소값을 구해서, 최소값과 자신을 비교해 최대값이 아니라면 answer에 하나씩 더해 리턴한다.
  3. 이 때, 단순히 min으로 최소값을 구하면 시간초과가 나게 된다.
  4. 왼쪽의 최소값은 일단 lft에 dq의 popleft값을 세팅하고, 순회할때마다 lft보다 현재 값이 작다면 현재 값을 lft에 저장하는 식으로 구현한다.
  5. 오른쪽의 최소값은 일단 a배열을 뒤집어 순회하면서, 각 자리마다 오른쪽에서부터 최소값을 세팅한다.
  6. 그 후 dq를 순회할때 각 index의 오른쪽 최소값을 빼서 비교하는 식으로 구현한다.
'''

from collections import deque

def solution(a):
    answer = 2
    dq = deque(a)
    cur = dq.popleft()
    idx = 1
    lft = cur
    rgt = [dq.pop()]
    b = a[-2::-1]
    for i in b:
      if i < rgt[-1]:
        rgt.append(i)
      else:
        rgt.append(rgt[-1])
    rgt.reverse()
    while dq:
      cur = dq.popleft()
      if lft > cur or rgt[idx + 1] > cur:
        answer += 1
      if lft > cur:
        lft = cur
      idx += 1
    return answer