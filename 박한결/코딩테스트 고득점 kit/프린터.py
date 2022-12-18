'''
풀이 및 접근방법

 1. location에 해당하는 위치값을 특정하기 위해 고유한 key값을 가진 딕셔너리 'dir'에 priorities를 저장한다.
 2. dir에서 location에 해당하는 key를 locateKey에 저장하고, key들을 담은 arr를 만든다.
 3. arr가 비어있을 때까지 아래의 로직을 반복한다.
  3-1. 만약 arr의 첫번째 값보다 큰 값이 하나라도 있다면 arr의 맨 뒤로 넘긴다.
  3-2. arr의 첫번째 값이 가장 큰 값이라면 arr2에 저장하면서 dir, arr에서 제거한다.
  3-3. 만약 3-1에 해당하지 않으면서 arr의 첫번째 값보다 큰 값이 없다면 arr2에 저장하면서 dir, arr에서 제거한다.
 4. arr2에서 locateKey의 위치값 + 1을 리턴한다.
'''

import string
import random

def solution(priorities, location):
  dir = {};
  resister = string.ascii_lowercase
  for i in priorities:
    dir[random.choice(resister)+random.choice(resister)+random.choice(resister)] = i
  arr = []
  arr2 = []
  for index, i in enumerate(dir.keys()):
    arr.append(i)
    if location == index:
      locateKey = i
  while len(arr) != 0:
    isMap = False
    isOver = False
    for index, i in enumerate(dir.values()):
      if dir[arr[0]] < i:
        arr.append(arr[0])
        arr.pop(0)
        isMap = True
        break
      elif index == len(arr) - 1:
        isOver = True
    if isMap == False and isOver == False:
      del dir[arr[0]]
      arr2.append(arr[0])
      arr.pop(0)
    elif isOver == True:
      for i in dir.values():
        if dir[arr[0]] == i:
          del dir[arr[0]]
          arr2.append(arr[0])
          arr.pop(0)
          break
  return arr2.index(locateKey) + 1
