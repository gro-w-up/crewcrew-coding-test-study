'''
풀이 및 접근방법
  1. 삼각형을 만들기 위해 n개의 빈 배열을 가진 리스트 arr을 세팅한다.
  2. 삼각형이 아래, 오른쪽, 위의 패턴대로 n개에서 1개씩 줄어들며 추가된다. 
     따라서 n을 하나씩 줄여가며 bottom, right, top으로 방향을 지정하며 순회한다.
  3. 방향이 bottom인 경우엔 시작되는 지점이 해당 패턴이 돌아올때마다 위에서 2, 왼쪽에서 1씩 증가한다.
     따라서 시작되는 지점을 변수로 세팅하고, 패턴이 끝나면 위에서 2, 왼쪽에서 1을 더한다.
  4. 방향이 right인 경우엔 시작되는 지점이 해당 패턴이 돌아올때마다 밑에서 1이 감소, 왼쪽에서 1씩 증가한다.
     따라서 시작되는 지점을 변수로 세팅하고, 패턴이 끝나면 밑에서 1을 빼고, 왼쪽에서 1을 더한다.
  5. 방향이 top인 경우엔 싲가되는 지점이 해당 패턴이 돌아올때마다 밑에서 1이 감소, 오른쪽에서 1씩 증가한다.
     따라서 시작되는 지점을 변수로 세팅하고, 패턴이 끝나면 밑에서 1을 빼고, 오른쪽에서 1을 더한다.
  6. 순회가 끝난 이중배열 arr를 평탄화해서 리턴한다.
'''

import itertools

def solution(n):
    arr = [[] for i in range(n)]
    direct = 'bottom'
    num = 1
    bottomStart = 0
    bottomLeftStart = 0
    rightStart = n - 1
    rightLeftStart = 1
    topStart = 2
    topRightStart = 0
    while n >= 1:
      if direct == 'bottom':
        for i in range(bottomStart, bottomStart + n):
          arr[i].insert(bottomLeftStart, num)
          num += 1
        direct = 'right'
        bottomStart += 2
        bottomLeftStart += 1
        n -= 1
        continue
      if direct == 'right':
        for i in range(0, n):
          arr[rightStart].insert(rightLeftStart + i, num)
          num += 1
        direct = 'top'
        rightStart -= 1
        rightLeftStart += 1
        n -= 1
        continue
      if direct == 'top':
        for i in range(0, n):
          if topRightStart == 0:
            arr[-topStart - i].append(num)
          else:
            arr[-topStart - i].insert(-topRightStart, num)
          num += 1
        direct = 'bottom'
        topStart += 1
        topRightStart += 1
        n -= 1
        continue
    return list(itertools.chain(*arr))