'''
풀이 및 접근방법

 1. 여벌 체육복을 가져왔지만 도난당한 경우의 수가 있기 때문에, 그 경우의 수를 뺀 lost와 reserve를 setlost, setreserve로 세팅한다.
 2. 앞사람에게 빌려준 경우를 matchedArr1, 뒷사람에게 빌려준 경우를 matchedArr2에 세팅한다.
 3. 두 경우의 수에서 중복을 뺀 리스트를 matchedArr3에 세팅한다.
 4. 체육복을 빌리지 못한 학생의 수를 islost에 세팅한 후, 전체 학생 수에서 islost를 뺀 값을 리턴한다.
'''

def solution(n, lost, reserve):
  lost.sort()
  reserve.sort()
  setlost = list(set(lost) - set(reserve))
  setreserve = list(set(reserve) - set(lost))
  matchedArr1 = []
  matchedArr2 = []
  for el in setlost:
    if el - 1 in setreserve:
      matchedArr1.append(el - 1)
    if el + 1 in setreserve:
      matchedArr2.append(el + 1)
  matchedArr3 = set(matchedArr1 + matchedArr2)
  islost = len(setlost) - len(matchedArr3)
  if islost < 0:
    islost = 0
  return n - islost