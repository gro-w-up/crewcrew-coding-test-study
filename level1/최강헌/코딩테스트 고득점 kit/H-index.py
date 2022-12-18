'''
풀이 및 접근방법
1.
2. array 정렬
3. 해당 인덱스 갖고오기
'''


def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        print(f'i = {i+1}')
        print(f'citations[{i}] = {citations[i]}')
        if i+1>citations[i]:
            return i

    return len(citations)
#print('result 1 : ', solution([3, 0, 6, 1, 5]))
print('result 1 : ', solution([10, 10, 10, 10, 10]))