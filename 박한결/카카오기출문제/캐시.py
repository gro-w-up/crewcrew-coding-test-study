'''
풀이 및 접근방법
  1. que에 cities의 첫번째 배열을 넣은 뒤, cities를 순회하며 반복한다.
  2. 만약 cachSize가 0이라면 항상 캐시처리가 되지 않으므로 cities의 길이에 5를 곱한 값을 리턴한다.
  3. 만약 cities의 q번째 값이 que에 있다면 que에서 해당 값을 뒤로 보낸 후, 1초를 더한다.
  4. 만약 que의 길이가 cachSize와 같다면 que의 첫번째 값을 없앤다.
  5. que에서 q번째 cities의 값을 추가한 후 5초를 더한다.
'''

from collections import deque

def solution(cacheSize, cities):
    answer = 5
    que = deque()
    que.append(cities[0].upper())
    q = 1
    while q <= len(cities) - 1:
      if cacheSize == 0:
        answer = len(cities) * 5
        break
      if cities[q].upper() in que:
        que.remove(cities[q].upper())
        que.append(cities[q].upper())
        answer += 1
        q += 1
        continue
      if len(que) >= cacheSize:
        que.popleft()
      que.append(cities[q].upper())
      answer += 5
      q += 1
          
    return answer