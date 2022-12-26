'''
풀이 및 접근방법

  1. 던전을 순회하는 모든 경우의 수를 순열을 통해 구한다.
  2. 경우의 수마다 던전을 클리어할 수 있는 횟수를 구해서 arr에 세팅한다.
  3. arr의 최대값을 리턴한다.
'''

import itertools

def solution(k, dungeons):
    perm = list(itertools.permutations(dungeons))
    arr = []
    for i in perm:
      pirodo = k
      clear = 0
      for need, spend in i:
        if pirodo >= need:
          pirodo -= spend
          clear += 1
      arr.append(clear)
    return max(arr)