'''
풀이 및 접근방법

  1. 최소 직사각형의 크기만 구하는 것이기에, 이 값이 가로냐 세로냐를 따질 필요가 없다.
  2. 따라서 가로, 세로 값 중 큰 값, 작은 값을 sort로 정렬해서 직사각형의 방향을 일치시킨다.
  3. 방향을 일치시킨 사각형의 길이값들 중 최대값을 구해서 곱해 크기값을 반환한다.
'''

def solution(sizes):
    arr1 = []
    arr2 = []
    for sizeEl in sizes:
      sizeEl.sort()
      arr1.append(sizeEl[0])
      arr2.append(sizeEl[1])
    return max(arr1) * max(arr2)