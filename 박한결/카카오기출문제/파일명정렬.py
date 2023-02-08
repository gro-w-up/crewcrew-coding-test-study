'''
풀이 및 접근방법
  1. files를 숫자를 기준으로 head, number, tail로 나누어 세팅해 arr에 세팅한다.
  2. head의 대문자를 기준으로 1차, number를 기준으로 2차조건으로 해서 arr을 정렬한다.
  3. arr의 원소들을 하나의 문자열로 합쳐서 answer에 넣은 후 리턴한다.
'''

import re

def solution(files):
    arr = []
    for i in files:
      arr.append(re.split("([0-9]+)", i, 1))
    arr.sort(key = lambda x: (x[0].upper(), int(x[1])))
    answer = []
    for i in arr:
      answer.append(''.join(i))
    return answer