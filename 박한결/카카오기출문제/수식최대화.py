'''
풀이 및 접근방법
  1. 주어진 expression을 숫자와 기호로 나눈다.
  2. + - *의 우선순위의 경우의 수를 susikArr에 세팅한다.
  3. susikArr의 경우의 수를 순회하며 각각의 경우의 수마다 결과값을 구한다.
   3-1. 경우의 수마다 그 기호가 없어질때까지, 그 기호의 앞과 뒤를 연산해 arr2에 세팅한다.
   3-2. 모든 기호가 없어지면 결과값의 절대값을 answer에 추가한다.
  4. answer의 최대값을 리턴한다.
'''

import re
import itertools
from collections import deque

def solution(expression):
    answer = []
    arr = re.split('([^0-9])', expression)
    susik = ['+', '-', '*']
    susikArr = deque(itertools.permutations(susik, 3))
    while susikArr:
      i = deque(susikArr.popleft())
      arr2 = arr.copy()
      while i:
        d = i.popleft()
        res = 0
        while d in arr2:
          for index, el in enumerate(arr2):
            if el == d:
              if d == '+':
                res = int(arr2[index - 1]) + int(arr2[index + 1])
                del arr2[index - 1]
                del arr2[index - 1]
                del arr2[index - 1]
                arr2.insert(index - 1, res)
                break
              elif d == '-':
                res = int(arr2[index - 1]) - int(arr2[index + 1])
                del arr2[index - 1]
                del arr2[index - 1]
                del arr2[index - 1]
                arr2.insert(index - 1, res)
                break
              elif d == '*':
                res = int(arr2[index - 1]) * int(arr2[index + 1])
                del arr2[index - 1]
                del arr2[index - 1]
                del arr2[index - 1]
                arr2.insert(index - 1, res)
                break
      answer.append(abs(arr2[0]))
    return max(answer)