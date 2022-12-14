'''
풀이 및 접근방법

 프로그래머스에 있는 문제 설명이 이해가 안돼서 3시간을 헤매다가 답을 찾아보고 나서야 이해가 됨...
 문제 설명이 좀 이상했던듯...

 1. bridge_length 값만큼 bridge 배열에 0을 넣어 다리길이만큼의 배열을 만든다.
 2. bridge배열이 모두 제거될때까지 다음을 반복한다.
  2-1. 반복과정에서 시간을 1씩 더하고, bridge의 첫번째를 지운다(통과를 완료하면 다리에서 없어지기 때문에).
  2-2. bridge 배열과 첫번째 대기 트럭의 무게값의 합이 weigth보다 작으면, bridge에 대기트럭을 append한다
  2-3. 2-2를 만족하지 않으면, 트럭이 올라갈 수 없기때문에 bridge에 0을 append한다.
'''

def solution(bridge_length, weight, truck_weights):
  answer = 0
  bridge = [0 for _ in range(bridge_length)]

  while bridge:
    answer += 1
    bridge.pop(0)
    if truck_weights:
      if sum(bridge) + truck_weights[0] <= weight:
        t = truck_weights.pop(0)
        bridge.append(t)
      else:
        bridge.append(0)
  return answer
