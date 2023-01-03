
'''
풀이 및 접근방법

 혼자 풀다가, 오른쪽으로 갈때랑 왼쪽으로 갈때가 같을때 처리가 안돼서 계속 틀림.
 풀이를 보고 붙여넣었는데 풀이를 봐도 이해가 잘안돼서 일단 보류.
'''



#가져온 풀이
def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            while n and n[-1] == 'A':
                n = n[:-1]

            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer


#혼자 풀다가 틀린 풀이
def equal(matchIndex, answer, arr, nameArr):
  while arr != nameArr:
    if arr[matchIndex] != nameArr[matchIndex]: #원소 바꾸기
      arr[matchIndex] = nameArr[matchIndex]
      if nameArr[matchIndex] <= 12:
        answer += nameArr[matchIndex]
      else:
        answer += (26 - nameArr[matchIndex])
    if arr == nameArr: #원소 바꾼 후 검사
      break

    rightMove = 0
    while True:
      if matchIndex + rightMove < len(arr):
        moveIndex = matchIndex + rightMove
      else:
        moveIndex = len(arr) - matchIndex + rightMove - 1
      if arr[moveIndex] == nameArr[moveIndex]:
        rightMove += 1
      else:
        break
        
    leftMove = 0
    while True:
      moveIndex = matchIndex - leftMove
      if arr[moveIndex] == nameArr[moveIndex]:
        leftMove += 1
      else:
        break
        
    if rightMove <= leftMove:
      matchIndex += rightMove
      answer += rightMove
    else:
      matchIndex -= leftMove
      answer += leftMove
  return answer
  

def solution(name):
  answer = 0
  arr = [0 for i in range(len(name))]
  nameArr = []
  for i in name:
    nameArr.append(ord(i) - 65)
  matchIndex = 0
  while arr != nameArr:
    if arr[matchIndex] != nameArr[matchIndex]: #원소 바꾸기
      arr[matchIndex] = nameArr[matchIndex]
      if nameArr[matchIndex] <= 12:
        answer += nameArr[matchIndex]
      else:
        answer += (26 - nameArr[matchIndex])
    print(arr == nameArr, arr, answer)
    if arr == nameArr: #원소 바꾼 후 검사
      break

    rightMove = 0 #오른쪽으로 이동
    while True:
      if matchIndex + rightMove < len(arr):
        moveIndex = matchIndex + rightMove
      else:
        moveIndex = len(arr) - matchIndex + rightMove - 1
      if arr[moveIndex] == nameArr[moveIndex]:
        rightMove += 1
      else:
        break
        
    leftMove = 0 #왼쪽으로 이동
    while True:
      moveIndex = matchIndex - leftMove
      if arr[moveIndex] == nameArr[moveIndex]:
        leftMove += 1
      else:
        break
        
    if rightMove < leftMove: #오른쪽이 더 짧으면
      matchIndex += rightMove
      answer += rightMove
    elif rightMove > leftMove: #왼쪽이 더 짧으면
      matchIndex -= leftMove
      answer += leftMove
    else: # 그외엔 둘 다 돌려서 더 짧은 것으로 선택
      matchIndex1 = matchIndex + rightMove
      matchIndex2 = matchIndex - leftMove
      answer1 = answer
      answer2 = answer
      arr1 = arr.copy()
      arr2 = arr.copy()
      def1 = equal(matchIndex1, answer1, arr1, nameArr)
      def2 = equal(matchIndex2, answer2, arr2, nameArr)
      if def1 < def2:
        matchIndex = matchIndex1
        answer += rightMove
      else:
        matchIndex = matchIndex2
        answer += leftMove
      
  return answer