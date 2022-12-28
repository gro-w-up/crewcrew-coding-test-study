'''
풀이 및 접근방법

 1. 8회를 넘으면 -1을 리턴하므로, 8까지만 반복한다.
 2. 같은 수가 연속으로 나오는 경우를 numbers에 세팅한다.
 3. numbers에 DP배열의 j번째와 마지막에서 j번째의 사칙연산 결과값들을 세팅한다.
 4. numbers 안에서 number가 발견되면 실행횟수 i를 리턴한다.

 https://gurumee92.tistory.com/164
'''

def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        numbers = set()
        numbers.add( int(str(N) * i) )
        
        for j in range(0, i-1):
            for x in DP[j]:
                for y in DP[-j-1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    
                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break
        
        DP.append(numbers)

    return answer