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