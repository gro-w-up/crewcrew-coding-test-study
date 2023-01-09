'''
풀이 및 접근방법
  1. 대소문자를 구분하지 않으므로, str1과 str2를 모두 대문자로 만든다.
  2. str1과 str2를 두글자씩 잘라서 arr1, arr2에 세팅한다. 이 때 알파벳이 아니라면 생략한다.
  3. 만약 arr1과 arr2가 0이라면 jakad에 1을 할당한다.
  4. 중복되는 경우를 대처하기 위해, dir1과 dir2에 arr1과 arr2의 원소를 key에, 중복되는 갯수를 value에 세팅한다.
  5. arr1과 arr2의 교집합, 합집합을 intsect, uni에 세팅한다.
  6. intersect를 순회하며 dir1과 dir2의 value값 중 최소값을 interLen에 더한다.
  7. uni를 순회하며 dir1과 dir2의 value값 중 최대값을 uniLen에 더한다.
  8. interLen/uniLen의 결과값을 jakad에 세팅하고, 그 값에서 65536을 곱하고 소수점을 버린 값을 리턴한다.
'''

import math, collections

def solution(str1, str2):
    jakad = 0
    STR1 = str1.upper()
    STR2 = str2.upper()
    arr1 = []
    arr2 = []
    for i in range(0, len(STR1) - 1):
      el = ''.join([STR1[i], STR1[i + 1]])
      if el.isalpha():
        arr1.append(el)
    for i in range(0, len(STR2) - 1):
      el = ''.join([STR2[i], STR2[i + 1]])
      if el.isalpha():
        arr2.append(el)
    if len(arr1) == 0 and len(arr2) == 0:
      jakad = 1
    else:
      dir1 = collections.defaultdict(int)
      dir2 = collections.defaultdict(int)
      for i in arr1:
        dir1[i] += 1
      for i in arr2:
        dir2[i] += 1
      intsect = set(arr1).intersection(set(arr2))
      uni = set(arr1).union(set(arr2))
      interLen = 0
      uniLen = 0
      for i in intsect:
        interLen += min(dir1[i], dir2[i])
      for i in uni:
        uniLen += max(dir1[i], dir2[i])
      jakad = interLen/uniLen
    answer = math.trunc(jakad * 65536)
    return answer