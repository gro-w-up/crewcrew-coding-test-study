'''
풀이 및 접근방법
  1. records를 공백 기준으로 자른 다음, 시간을 시*60 + 분으로 계산해서 arr에 세팅한다.
  2. arr를 순회하며, IN일때는 cars에 차번호를 key값, 들어온 시간을 value값으로 세팅한다.
  3. OUT일때는 레코드의 나간 시간에서 들어온 시간을 뺀 값을 value값에 더한 후, 들어온 시간을 초기화한다.
  4. 만약 모든 arr를 순회한 후에도 들어온 시간이 남아있거나 0시에 들어온 경우, 23시 59분에서 들어온 시간을 뺀 값을 value값에 더한다.
  5. cars를 key값을 기준으로 정렬한다.
  6. 모든 차들의 주차 시간이 담긴 cars를 순회하며 주차요금을 계산한다. 만약 계산간 값이 기본요금보다 낮으면 기본요금으로 세팅한다.
  7. 계산된 값들이 담긴 answer를 리턴한다.
'''

from collections import deque, defaultdict
import math

def solution(fees, records):
  answer = []
  arr = []
  cars = defaultdict(list)
  for i in records:
    j = i.split()
    k = j[0].split(':')
    time = int(k[0]) * 60 + int(k[1])
    arr.append([time, j[1], j[2]])
  dq = deque(arr)
  while dq:
    record = dq.popleft()
    if record[2] == 'IN':
      if record[1] not in cars:
        cars[record[1]] = [int(record[0]), 0]
      else:
        cars[record[1]][0] = int(record[0])
    elif record[2] == 'OUT':
      cars[record[1]][1] += int(record[0]) - cars[record[1]][0]
      cars[record[1]][0] = 0
  for key, value in cars.items():
    if value[0] != 0:
      cars[key][1] += (23*60 + 59) - value[0]
    elif value[0] == 0 and value[1] == 0:
      cars[key][1] += (23*60 + 59) - value[0]
  cars2 = sorted(cars.items())
  for i in cars2:
    answer.append(fees[1] + math.ceil((i[1][1] - fees[0])/fees[2]) * fees[3])
  for idx, i in enumerate(answer):
    if i < fees[1]:
      answer[idx] = fees[1]
  return answer