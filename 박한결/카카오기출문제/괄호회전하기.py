'''
풀이 및 접근방법
  1. 주어진 문자열 s를 회전하면서 arr에 세팅한다.
  2. 회전한 arr의 원소값들을 순회하면서 checkValid 함수를 실행한다.
   2-1. 만약 주어진 값 s가 ), ], }로 시작하면 false를 반환한다.
   2-2. s를 dq에 deque로 세팅한 후, dq의 길이가 존재하면 다음을 순회한다.
    2-2-1. dq의 첫번째 값이 (, [, {이면 stack에 추가한다.
    2-2-2. dq의 첫번쨰 값이 ), ], }이면 stack이 비면 함수가 false를 반환한다.
    2-2-3. 아니라면 만약 stack의 마지막 값이 대응하는 괄호라면 stack에서 마지막 값을 뺀다.
   2-3. 모두 순회한 후 stack이 남아있으면 false, 없으면 true를 반환한다.
  3. checkValid 함수의 결과값들이 담긴 arr2에서 true의 갯수를 리턴한다. 
'''

from collections import deque

def checkValid(s):
  if s[0] == ')' or s[0] == ']' or s[0] == '}':
    return False
  dq = deque(s)
  stack = []
  while dq:
    chd = dq.popleft()
    if chd == ')':
      if len(stack) == 0:
        return False
      elif stack[-1] == '(':
        stack.pop()
    elif chd == '(': 
      stack.append(chd)
    if chd == ']':
      if len(stack) == 0:
        return False
      elif stack[-1] == '[':
        stack.pop()
    elif chd == '[':
      stack.append(chd)
    if chd == '}': 
      if len(stack) == 0:
        return False
      elif stack[-1] == '{':
        stack.pop()
    elif chd == '{':
      stack.append(chd)
  if stack:
    return False
  else:
    return True
  
def solution(s):
    arr = []
    for i in range(len(s)):
      arr.append(''.join([s[i:],s[0:i]]))
    arr2 = []
    for i in arr:
      arr2.append(checkValid(i))
    answer = 0
    for i in arr2:
      if i == True:
        answer += 1
    return answer