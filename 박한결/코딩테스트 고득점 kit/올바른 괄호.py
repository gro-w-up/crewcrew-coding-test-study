'''
풀이 및 접근방법

 1. 일단 주어지는 s문자열이 ")"로 시작하거나 빈 문자열이면 false를 반환한다.
 2. 문자열을 순회하며 "("일땐 isTrue를 1씩 증가, ")"일땐 감소 시킨다.
    이 때 isTrue가 양수일 때만 감소하게 해서 괄호의 갯수만 맞고 순서가 맞지 않을 때 True를 반환하지 않게 한다.
 3. isTrue가 0이 아니라면 False, 0이라면 True를 반환한다.
'''

def solution(s):
  answer=True
  isTrue = 0
  if len(s)== 0 or s[0] ==")":
    return False
  for l in s:
    if l == "(":
      isTrue+=1
    else:
      if isTrue > 0:
        isTrue-=1
  if isTrue!=0:
    answer = False
  return answer