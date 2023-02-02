'''
풀이 및 접근방법
  1. 주어진 매개변수를 이진변환하는 함수 izin을 만든다.
  2. 문자열 s가 1이 될 떄까지 순회하며 izin을 실행해, 실행한 횟수와 0의 갯수를 리턴한다.
'''


zero = 0
def izin(s):
  global zero
  letter = []
  for i in s:
    if i == '1':
      letter.append(i)
    if i == '0':
      zero += 1
  return str(bin(len(letter))[2:])
def solution(s):
    global zero
    tryN = 0
    while s != '1':
      s = izin(s)
      tryN += 1
    return [tryN, zero]