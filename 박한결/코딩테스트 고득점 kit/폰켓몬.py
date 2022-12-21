'''
풀이 및 접근방법
  nums/2만큼 가져갈 수 있지만, 중복된 값이 존재하므로
  nums/2와 중복을 제거한 nums의 길이 중 최소값을 반환한다.

'''

import math

def solution(nums):
  numSet = set(nums)
  lenN = math.ceil(len(nums) / 2)
  return min(lenN, len(numSet))