'''
풀이 및 접근방법
  1. board의 원소들을 한 글자씩 잘라서 arr에 세팅한다.
  2. arr를 deque로 세팅해 하나씩 popleft로 빼면서 순회한다.
  3. 각 좌표의 오른쪽, 아래쪽, 오른쪽 아래가 자신과 같다면 삭제할 좌표값을 delArr에 추가한다.
  4. delArr에서 중복을 제거한 후 해당 좌표를 빈 문자열로 치환한다.
  5. arr를 뒤에서 앞으로 순회하며, 남은 블록들을 제거된 문자열과 자리를 바꾼다.
  6. 제거된 블록의 수를 리턴한다.
'''

from collections import deque

def solution(m, n, board):
    answer = 0
    arr = [list(i) for i in board]
    while True:
      dq = deque(arr)
      i = 0
      delArr = []
      while dq and i + 1 < len(board):
        j = dq.popleft()
        for idx, el in enumerate(j):
          if idx + 1 >= len(j):
            break
          if el == '':
            continue
          if arr[i][idx + 1] == el and arr[i + 1][idx] == el and arr[i + 1][idx + 1] == el:
            delArr.append((i, idx))
            delArr.append((i + 1, idx))
            delArr.append((i + 1, idx + 1))
            delArr.append((i, idx + 1))
        i += 1
      delArr = list(set(delArr))
      if len(delArr) == 0:
        break
      answer += len(delArr)
      deldq = deque(delArr)
      while deldq:
        k = deldq.popleft()
        arr[k[0]][k[1]] = ''
      i = len(arr) - 2
      while i >= 0:
        for idx, el in enumerate(arr[i]):
          if el == '':
            continue
          j = i
          while j + 1 < len(arr):
            if arr[j + 1][idx] != '':
              break
            arr[j + 1][idx] = el
            arr[j][idx] = ''
            j += 1
        i -= 1
      
    return answer