from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff, max_comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11), n):
        cnt = Counter(comb)
        lscore, ascore = 0, 0

        for i in range(1, 11):
            if info[10-i] < cnt[i]:
                lscore += i
            elif info[10-i] > 0:
                ascore += i

        diff = lscore - ascore
        if diff > max_diff:
            max_comb_cnt = cnt
            max_diff = diff

    if max_diff > 0:
        answer = [0] * 11
        for n in max_comb_cnt:
            answer[10-n] = max_comb_cnt[n]
        return answer
    else:
        return [-1]