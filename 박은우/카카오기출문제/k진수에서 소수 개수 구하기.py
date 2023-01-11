import string
import math

tmp = string.digits + string.ascii_lowercase


def solution(n, k):
    answer = 0

    trans_number = convert(n, k)
    print('trans_number = {}'.format(trans_number))
    for n in trans_number.split('0'):
        print('n = {}'.format(n))
        if n == "":
            continue
        if primenumber(int(n)):  # n이 소수인 경우 answer+=1
            answer += 1

    return answer


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def primenumber(x):
    if x == 2 or x == 3: return True  # 2 or 3 은 소수
    if x % 2 == 0 or x < 2: return False  # 2의 배수이거나 2보다 작은 값인 경우 소수가 아님

    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


# expect 3
print(solution(437674, 3))
# expect 3
print(solution(110011, 10))

"""
참고자료 
    - 진법 변환 : https://security-nanglam.tistory.com/508
"""
"""
실행 결과
테스트 1 〉	통과 (120.05ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.5MB)
테스트 5 〉	통과 (0.02ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.5MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.03ms, 10.5MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.6MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
테스트 16 〉	통과 (0.03ms, 10.4MB)
"""