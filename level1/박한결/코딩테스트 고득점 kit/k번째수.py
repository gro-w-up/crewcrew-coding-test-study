'''
풀이 및 접근방법

 다음과 같이 commands의 각 배열 요소들을 반복해서 arr리스트에 저장한 후 리턴한다.
  1. commands의 첫번째 요소부터 두번째 요소까지 array를 자른다.
  2. 자른 결과를 정렬한다.
  3. 그 결과물에서 commands의 세번째 요소값 -1번째 자리를 arr리스트에 저장한다.
'''

def solution(array, commands):
    arr = []
    for start, last, index in commands:
      slice = array[start - 1: last]
      slice.sort()
      arr.append(slice[index - 1])
    answer = arr
    return answer