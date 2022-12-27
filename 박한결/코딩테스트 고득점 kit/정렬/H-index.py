'''
풀이 및 접근방법
  문제 해설이 모호한데, h의 기준이 인용된 논문의 갯수에 있기 때문에 h는 citations의 원소들이 아니라 citations의 갯수에서 찾아야 한다.

  1. 0부터 citations의 길이값까지의 범위를 인덱스 h로 잡고 다음을 반복한다.
   1-1. citations의 원소들 중 h이상 값의 갯수를 count에 저장한다.
   1-2. citations의 원소들 중 h미만 값의 갯수를 count2에 저장한다.
   1-3. count가 h이상이고, count2가 h이하일 때 arr에 저장한다.
  2. 반복문의 결과 arr의 최대값을 리턴한다.
'''

def solution(citations):
    arr = []
    for h in range(0, len(citations) + 1):
      count = 0
      count2 = 0
      for el in citations:
        if el >= h:
          count += 1
        else:
          count2 += 1
      if count >= h and count2 <= h:
        arr.append(h)
    return max(arr)