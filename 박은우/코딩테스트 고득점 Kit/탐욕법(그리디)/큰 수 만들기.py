# 1번 풀이
# from itertools import combinations
# def solution(number, k):
#     print('-------')
#     print(list(combinations(number, len(number) - k)))
#     return ''.join(sorted(list(combinations(number, len(number) - k)), reverse=True)[0])

# 2번풀이
# def solution(number, k):
#     stack = []
#
#     for num in number:
#
#         while stack and stack[-1] < num and k > 0:
#             print('stack : {}, stack[-1] : {}, num : {}, k : {}'.format(stack, stack[-1], num, k))
#             stack.pop()
#             k -= 1
#         stack.append(num)
#
#     return ''.join(stack)

# 3번풀이
def solution(number, k):
    stack = []

    for num in number:

        while stack and stack[-1] < num and k > 0:
            # print('stack : {}, stack[-1] : {}, num : {}, k : {}'.format(stack, stack[-1], num, k))
            stack.pop()
            k -= 1
        stack.append(num)

    # 내림차순 되어 있는 number일 경우
    if k > 0 :
        stack = stack[:-k]

    return ''.join(stack)

# expect 94
print(solution("1924", 2))
# expect 3234
print(solution("1231234", 3))
# expect 775841
print(solution("4177252841", 4))
# expect 5432
print(solution("54321", 1))


"""
def solution(number, k):
    스택 초기화

    for num in 전달받은 number 파라미터:

        while 스택이 비어있지 않고 and 마지막 값 < 현재 숫자 and k개의 수 > 0 (남아있음):
            결과의 마지막 요소 제거
            k개의 수 -1
        스택에 현재 num 저장

    return ''.join(stack)
"""
"""
[1번 풀이]
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.10ms, 10.1MB)
테스트 2 〉	통과 (2131.35ms, 487MB)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
채점 결과
정확성: 33.3
합계: 33.3 / 100.0
"""
"""
[2번 풀이]
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (0.15ms, 10.1MB)
테스트 6 〉	통과 (2.95ms, 10.2MB)
테스트 7 〉	통과 (6.69ms, 10.5MB)
테스트 8 〉	통과 (15.11ms, 10.4MB)
테스트 9 〉	통과 (62.35ms, 12.6MB)
테스트 10 〉	통과 (83.00ms, 12.8MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	실패 (0.00ms, 10.1MB)
"""