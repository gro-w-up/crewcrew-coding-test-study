def solution(k, dungeons):
    return search(k, dungeons, 0)

def search(k, dungeon_list, count):

    print('피로도 : {} 탐색한 던전 수: {}  남은 던전: {}'.format(k, count, dungeon_list))

    # 탐색한 던전 수
    count_list = [count]

    # 주어진 던전 개수 만큼 반복한다.
    for i in range(len(dungeon_list)):
        # 던전의 소모 피로도가 현재 피로도보다 작으면
        if dungeon_list[i][0] <= k:
            # dungeon_list의 임시 리스트 만들고
            temp_list = dungeon_list.copy()
            # 던전을 돌았다고 판단해서 리스트에서 지운다.
            del temp_list[i]
            # 피로도 계산, 남은 던전 리스트, 탐색한 던전 수를 재귀 호출한다.
            # 탐색한 던전들의 건수를 저장하는 배열에 추가
            count_list.append(search(k - dungeon_list[i][1], temp_list, count + 1))
            if count == 0:
                print('----------------------------------------------')

    print('탐색한 던전 수를 저장한 리스트 : {}'.format(count_list))
    return max(count_list)


# expect 3
print(solution(80, [[80,20],[50,40],[30,10]]))

"""
접근 및 풀이 방법
    - 문제 단순화
        1. k = 현재 피로도
        2. dungeons = [[최소피로도, 소모 피로도], ...]
        3. 만약, 1 -> 3 -> 2로 순서로 탐험 하게 된다면
        4. 피로도가 10남고, 3개의 던전으 모두 탐험할 수 있게됨.
    - 접근 방법
"""