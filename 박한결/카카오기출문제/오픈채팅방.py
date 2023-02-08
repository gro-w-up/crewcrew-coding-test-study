'''
풀이 및 접근방법
  1. record를 공백 기준으로 자른 후, 유저가 입장하거나 닉네임을 바꿀때마다 users에 아이디와 닉네임을 세팅한다.
  2. record를 순회하며 명령어와 아이디에 맞게 메시지를 리턴한다.
'''

from collections import deque, defaultdict

def solution(record):
    answer = []
    arr = []
    users = defaultdict(list)
    for i in record:
      arr.append(i.split())
    dq = deque(arr)
    while dq:
      i = dq.popleft()
      if i[0] == 'Enter' or i[0] == 'Change':
        if i[2]:
          users[i[1]] = i[2]

    dq = deque(arr)
    while dq:
      i = dq.popleft()
      if i[0] == 'Enter':
        answer.append(users[i[1]] + '님이 들어왔습니다.')
      elif i[0] == 'Leave':
        answer.append(users[i[1]] + '님이 나갔습니다.')
    return answer
