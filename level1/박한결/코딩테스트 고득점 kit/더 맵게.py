'''
풀이 및 접근방법
  1. scoville를 heapify로 재구성한다.
  2. scoville의 최소값이 K보다 작지 않을때까지 다음을 반복한다.
    2-1. scoville에서 첫번째, 두번째 요소를 빼서 각각 변수에 담는다.
    2-2. scoville에 두 요소를 섞은 값을 넣는다.
    2-3. 만약 반복과정에서 scoville의 길이가 2보다 작아지면 -1를 리턴하고 반복문을 정지한다.
    2-4. 반복하면서 answer를 1씩 증가시킨다.
  3. 반복문의 결과 answer를 반환한다.
 
 그런데 밑의 통과안된 코드처럼, 섞을 값을 blend로 따로 저장하면 왜 통과가 안되는지 이해가 안됨.
'''

import heapq

def solution(scoville, K):
  answer = 0
  heapq.heapify(scoville)
  while scoville[0] < K:
    if len(scoville) < 2:
      answer = -1
      break
    current = heapq.heappop(scoville)
    nextCurrent = heapq.heappop(scoville)
    heapq.heappush(scoville, current + nextCurrent*2)
    answer += 1
  return answer



 # 통과 안된 코드

def solution(scoville, K):
  answer = 0
  heapq.heapify(scoville)
  blend = 0
  while blend < K:
    blend = 0
    if len(scoville) < 2:
      answer = -1
      break
    current = heapq.heappop(scoville)
    nextCurrent = heapq.heappop(scoville)
    blend += current + nextCurrent * 2
    answer += 1
    heapq.heappush(scoville, blend)
    print(scoville)
  return answer