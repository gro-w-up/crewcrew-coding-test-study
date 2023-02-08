'''
풀이 및 접근방법
  1. n을 k진수로 바꾸는 함수 jin을 실행한 후, 그 값을 0으로 잘라 num에 세팅한다.
  2. num을 순회하며 1이 아니라면 소수를 반별하는 isprime을 실행해, 소수이면 answer를 1씩 증가한다.
  3. answer를 리턴한다.
'''

import math

def jin(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def isprime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    num = jin(n, k).split('0')
    answer = 0
    for i in num:
      if i == '':
        continue
      if int(i) == 1:
        continue
      if isprime(int(i)) == True:
        answer += 1
    return answer