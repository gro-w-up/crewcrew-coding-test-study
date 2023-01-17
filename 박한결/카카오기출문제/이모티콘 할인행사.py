'''
풀이 및 접근방법
  1. 할인율의 경우의 수를 중복순열을 통해 sales로 세팅하고, 경우의 수에 따른 구매액수를 temp에 0원으로 세팅한다.
  2. sales를 순회하며, 각 경우의 수에 따른 유저들의 구매액수를 구해 temp에 세팅한다.
  3. temp를 순회하며 users마다 구매 비용을 초과해 서비스에 가입하는 경우를 True로 변환한 후 arr에 담는다.
  4. arr에서 True의 갯수와 구매한 액수를 이중조건으로 sort한 후, 조건에 맞는 결과를 리턴한다.
'''

from collections import deque
from itertools import product
import math

def solution(users, emoticons):

  sales = list(product([10, 20, 30, 40], repeat = len(emoticons)))
  temp = [[0 for e in range(len(users))] for i in range(len(sales))]
  i = 0
  sldeq = deque(sales)
  while sldeq:
    sale = sldeq.popleft()
    usdeq = deque(users)
    i2 = 0
    while usdeq:
      ussl, uspr = usdeq.popleft()
      for idx, el in enumerate(emoticons):
        if sale[idx] >= ussl:
          temp[i][i2] += el - (el * sale[idx] / 100)
      i2 += 1
    for idx, e in enumerate(temp[i]):
      if e >= users[idx][1]:
        temp[i][idx] = True
    i += 1
  arr = []
  for i in temp:
    if True in i:
      arr.append(i)
  if len(arr) == 0:
    tmpst = sorted(temp, key=lambda x: (sum(x)))
    return [0,math.ceil(sum(tmpst[-1]))]
  arr.sort(key=lambda x: (x.count(True), sum(x)))
  answer = [arr[-1].count(True), 0]
  for i in arr[-1]:
    if i != True:
      answer[1] += i
  return answer