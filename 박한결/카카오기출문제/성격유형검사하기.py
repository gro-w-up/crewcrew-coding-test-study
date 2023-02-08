'''
풀이 및 접근방법
  1. 각 성격유형을 mbti에 세팅한다.
  2. survey를 한글자씩 자른후 deque로 만들어 dq에 세팅한다.
  3. dq를 순회하며, 해당하는 choices가 4점인 경우 생략, 4점 미만인 경우 앞쪽 항목, 4점 초과인 경우 뒤쪽 항목에 점수를 추가한다.
  4. 각 성격유형 중 더 높은 점수의 유형을 뽑아 리턴한다.
'''


from collections import deque

mbti = {
  'R': 0,
  'T': 0,
  'C': 0,
  'F': 0,
  'J': 0,
  'M': 0,
  'A': 0,
  'N': 0
}

def solution(survey, choices):
    arr = [list(i) for i in survey]
    dq = deque(arr)
    i = 0
    while dq:
      da, a = dq.popleft()
      if choices[i] == 4:
        i += 1
        continue
      if choices[i] < 4:
        mbti[da] += 4 - choices[i]
      if choices[i] > 4:
        mbti[a] += choices[i] - 4
      i += 1
    answer = ''
    if mbti['R'] >= mbti['T']:
      answer += 'R'
    elif mbti['R'] < mbti['T']:
      answer += 'T'
    if mbti['C'] >= mbti['F']:
      answer += 'C'
    elif mbti['C'] < mbti['F']:
      answer += 'F'
    if mbti['J'] >= mbti['M']:
      answer += 'J'
    elif mbti['J'] < mbti['M']:
      answer += 'M'
    if mbti['A'] >= mbti['N']:
      answer += 'A'
    elif mbti['A'] < mbti['N']:
      answer += 'N'
    return answer