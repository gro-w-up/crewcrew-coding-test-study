'''
풀이 및 접근방법


'''

from collections import defaultdict

def solution(clothes):
    cloth = defaultdict(int)

    for name, kind in clothes:
        cloth[kind] += 1

    answer = 1
    for i in cloth.values():
        answer *= (i + 1)

    return answer - 1