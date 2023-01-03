'''
https://cocook.tistory.com/113 참조 1
https://www.youtube.com/watch?v=ZsVVTEfZee8 동영상 강의 시청
'''


def solution(N, number):
    # 1. dp[i]는 N을 i 번만 사용해서 만들수 있는 집합.,,?
    # 예시) 5,55,555,5555,55555,555555...
    # 정답을 봐도 모르겠따,,,,,,,,,,,,,,,,,,,,,,,,,,
    dp = [set([N * int('1' * i)]) for i in range(1, 9)]
    print(dp)
    for i in range(8):  # N을 사용한 횟수
        for j in range(i):
            for num1 in dp[j]:  # i 번 사용해서 나타낼 수 있는 수
                for num2 in dp[i - j - 1]:  # N-i번 사용해서 나타낼 수 있는 수
                    # 사칙연산
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)

        # 위 과정을 끝내면 N을 i번 사용해서 나타낼 수있는 수가 dp[i]에 저장된다.
        # 만약 그 집합안에 'number'가 있으면
        if number in dp[i]:
            return i + 1  # 정답 출력
    return -1


def solution2(N, number):
    answer = 0
    # 큰 문제 - > 여러개의 작은 문제들로 쪼개어 접근?
    _li = [set() for i in range(8)]

    for i in range(len(_li)):
        _li[i].add(int(str(N)) * (i + 1))

    for i in range(1, 8):  # 1부터 시작하는 이유는, 첫번째는 {5}와 같이 연산 할 것이 없어서
        for j in range(i):
            for op1 in _li[j]:
                for op2 in _li[i - j - 1]:
                    _li[i].add(op1 + op2)
                    _li[i].add(op1 - op2)
                    _li[i].add(op1 * op2)
                    if op2 != 0:
                        _li[i].add(op1 // op2)
        if number in _li[i]:
            answer = i + 1
            break
    return answer

# print(solution(5, 12))
print(solution2(5, 12))
