from itertools import permutations

def solution(k, dungeons):
    answer = -1

    for dungeons in permutations(dungeons, len(dungeons)):
        temp = k
        dungeon_cnt = 0
        for dungeon in dungeons:
            need, consume = dungeon

            if temp >= need:
                dungeon_cnt += 1
                temp -= consume

        answer = max(answer, dungeon_cnt)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))