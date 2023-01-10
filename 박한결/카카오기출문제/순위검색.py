'''
풀이 및 접근방법
  1. 모든 검색결과에 따른 점수의 경우의 수를 반환해야 한다.
   1-1. True, False가 총 4개씩 배치되는 모든 경우의 수가 있는 리스트 binarys를 세팅한다.
   1-2. info 안에서 binarys를 이중순회하며, binarys의 원소가 True이면 info의 원소, False이면 '-'가 들어가는 원소들을 infomap의 key에 세팅한다.
   1-3. 결과적으로 info에 들어가는 모든 원소의 경우의 수 + '-'가 들어가는 경우의 수가 infomap의 key값에 세팅된다.
   1-4. binarys를 순회할 때, infomap[key]에 점수값을 추가한다.
  2. query를 순회하며, 각 원소들을 점수를 제외한 문자열들을 'and'를 빼고 합친다.
  3. 합친 문자열 key와 일치하는 infomap[key]에서, 이진탐색을 통해 나온 위치값보다 오른쪽에 있는 점수들의 갯수를 answers에 더해 리턴한다.
'''

import bisect, itertools, collections

def solution(info, query):
    infomap = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    for inf in info:
        inf = inf.split()
        
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)])
            infomap[key].append(int(inf[4]))
    for k in infomap.keys():
        infomap[k].sort()
    answers = []
    for q in query:
        l,_,p,_,c,_,f, point = q.split()
        key = ''.join([l,p,c,f])
        i = bisect.bisect_left(infomap[key], int(point))
        answers.append(len(infomap[key]) - i)

    return answers