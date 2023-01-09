'''
풀이 및 접근방법
  문제를 보자말자 이전에 풀었던 N으로 표현이 생각남. 같은 로직으로 풀기로 결정.
  1. numbers의 첫번째 숫자를 양수, 음수로 나눠 dp배열에 세팅한다.
  2. 0에서 numbers의 길이만큼 i범위를 지정한 후 다음을 반복한다.
   2-1. i번째 dp의 원소들과 numbers의 i번째 수를 빼고 더한 값을 arrset에 저장한다.
   2-2. 계산값들이 저장된 arrset을 dp에 추가한다.
  3. 최종적으로 계산된 값이 저장된 dp의 마지막 결과값들에서 target과 일치하는 값의 갯수를 리턴한다.
'''

def solution(numbers, target):
    answer = 0
    dp = [[numbers[0], numbers[0] * -1]]
    for i in range(0, len(numbers) - 1):
      arrset = []
      for x in dp[i]:
          arrset.append(x + numbers[i+1])
          arrset.append(x - numbers[i+1])
      dp.append(arrset)
    for i in dp[-1]:
      if i == target:
        answer+=1
    return answer