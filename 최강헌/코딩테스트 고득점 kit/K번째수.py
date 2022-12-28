'''
풀이 및 접근방법
1. array 개수에 따라 자르기
2. array 정렬
3. 해당 인덱스 갖고오기
'''


def solution(array, commands):
    result = list()
    for start, end, index in commands:
    # 해당 인덱스갖고오기 시작 숫자~ 끝숫자
        splitArray = array[start-1:end]
    # 정렬
        splitArray.sort()
    # 출력
        result.append(splitArray[index-1])
    return result

print('result 1 : ', solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
