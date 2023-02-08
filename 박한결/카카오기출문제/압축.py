'''
풀이 및 접근방법
  1. 만약 탐색하는 msg의 i번째가 마지막이라면, answer에 dict의 key i에 해당하는 value를 추가한다.
  2. 아니라면, msg의 i번째부터 뒤로 한 글자씩 늘리면서 dict에 존재하는지 검사한다.
  3. 존재하는 가장 긴 값을 nowStr, 추가해야 하는 값을 appendStr에 세팅한다.
  4. 탐색된 값의 길이를 i에 더하고, i가 msg의 길이와 같아질때까지 반복한다.
'''

dict = {
  'A': 1,
  'B': 2,
  'C': 3,
  'D': 4,
  'E': 5,
  'F': 6,
  'G': 7,
  'H': 8,
  'I': 9,
  'J': 10,
  'K': 11,
  'L': 12,
  'M': 13,
  'N': 14,
  'O': 15,
  'P': 16,
  'Q': 17,
  'R': 18,
  'S': 19,
  'T': 20,
  'U': 21,
  'V': 22,
  'W': 23,
  'X': 24,
  'Y': 25,
  'Z': 26
}

def solution(msg):
    answer = []
    i = 0
    id = 1
    while i <= len(msg) - 1:
        if i == len(msg) - 1:
          answer.append(dict[msg[i]])
          break
        l = 1
        nowStr = msg[i]
        appendStr = msg[i]
        while True:
          if i + l == len(msg) + 1:
            break
          elif msg[i:i+l] in dict:
            nowStr = msg[i:i+l]
            l += 1
          else:
            appendStr = msg[i:i+l]
            break
        dict[appendStr] = 26 + id
        answer.append(dict[nowStr])
        id+=1
        if l == 1:
          i += 1
        else:
          i += l-1
    return answer