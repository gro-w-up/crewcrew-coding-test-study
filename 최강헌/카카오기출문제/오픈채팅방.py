'''
1. 배열 분리
2. map에 삽입
3. 명령어에 따른 result 추가
'''


def solution(record):
    answer = []
    user = dict()

    for val in record:
        split = val.split(" ")
        if split[0] == "Enter":
            user[split[1]] = split[2]
        elif split[0] == "Change":
            user[split[1]] = split[2]

    for val in record:
        val_split = val.split(" ")
        if val_split[0] == "Enter":
            answer.append('%s님이 들어왔습니다.' % user[val_split[1]])
        if val_split[0] == "Leave":
            answer.append('%s님이 나갔습니다.' % user[val_split[1]])


    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
