'''
풀이 및 접근방법

 1. 일단 옷의 종류에 따라 분류해야 하므로 딕셔너리 'dir'에 종류를 key로 해서 종류별 옷의 가짓수를 저장한다.
 2. 옷의 조합만 하면 되므로 옷의 종류별 갯수를 배열 'arr'에 저장한다.
 3. 반복문을 통해 옷의 조합 경우의 수를 구한다.
  ex) arr가 [2,1,1]인 경우 (2 + 2*1 + 2*1*1) + (1 + 1*1) + 1
'''

def solution(clothes):
  answer = 0
  dir = {}
  for cloth, type in clothes:
    if type not in dir:
      dir[type] = 1
    else:
      dir[type] = dir[type] + 1
  arr = []
  for key in dir.keys():
    arr.append(dir[key])
  for i, e in enumerate(arr):
    sumEl = 0
    for el in arr[i:]:
      if sumEl == 0:
        sumEl += el
      else:
        sumEl += sumEl*el
    answer += sumEl
  return answer
