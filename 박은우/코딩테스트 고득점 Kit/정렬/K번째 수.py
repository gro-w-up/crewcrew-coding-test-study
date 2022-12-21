def solution(array, commands):
    answer = []

    for command in commands:
        start, end, k = command
        answer.append(list(sorted(array[start - 1:end]))[k - 1])

        # indexArray = []
        # while start <= end:
        #     indexArray.append(array[start-1])
        #     start += 1

        # answer.append(sorted(indexArray)[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

"""
접근 및 풀이 방법
    - 문제 단순화
        1치원 배열 array의 
        i번째 숫자부터 j번째 숫자까지 자르고
        정렬했을 때, 
        k번째에 있는 수를 구한다.
    - 접근 방법
         array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
         1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
         2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
         3. 2에서 나온 배열의 3번째 숫자는 5입니다.
"""

"""
다른 사람의 풀이
    list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
"""