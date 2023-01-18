def solution(record):

    process = []
    user_dic = {}

    for line in record:

        print('process = {}'.format(process))
        recodes = line.split()
        event = recodes[0]
        uid = recodes[1]


        if 'Leave' == event:
            process.append(uid)
            process.append('님이 나갔습니다.#')
        if 'Enter' == event:
            process.append(uid)
            process.append('님이 들어왔습니다.#')
            nickname = recodes[2]
            user_dic[uid] = nickname
        if 'Change' == event:
            nickname = recodes[2]
            user_dic[uid] = nickname

    print('--------------------')

    check_process = ''.join(process)
    answer = check_process.split('#')
    answer.pop()
    # 이벤트 처리 완료
    print('answer = {}'.format(answer))
    print('--------------------')
    for index, value in enumerate(answer):
        key = value.split('님')[0]
        print('[DEBUG] key = {}, value = {}, user_dic.get(key) = {}'.format(key, value, user_dic.get(key)))
        answer[index] = value.replace(key, user_dic.get(key))
    print('--------------------')
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

"""
실행 결과
채점을 시작합니다.
정확성  테스트
테스트  1 〉	통과 (0.03ms, 10.1MB)
테스트  2 〉	통과 (0.02ms, 10.3MB)
테스트  3 〉	통과 (0.05ms, 10.3MB)
테스트  4 〉	통과 (0.06ms, 10.3MB)
테스트  5 〉	통과 (0.71ms, 10.5MB)
테스트  6 〉	통과 (0.81ms, 10.4MB)
테스트  7 〉	통과 (0.69ms, 10.3MB)
테스트  8 〉	통과 (1.42ms, 10.2MB)
테스트  9 〉	통과 (1.70ms, 10.4MB)
테스트 10 〉	통과 (0.95ms, 10.5MB)
테스트 11 〉	통과 (0.48ms, 10.3MB)
테스트 12 〉	통과 (0.51ms, 10.1MB)
테스트 13 〉	통과 (0.79ms, 10.3MB)
테스트 14 〉	통과 (1.23ms, 10.4MB)
테스트 15 〉	통과 (0.02ms, 10.1MB)
테스트 16 〉	통과 (0.02ms, 10.4MB)
테스트 17 〉	통과 (0.10ms, 10.1MB)
테스트 18 〉	통과 (0.14ms, 10.4MB)
테스트 19 〉	통과 (1.55ms, 10.5MB)
테스트 20 〉	통과 (0.76ms, 10.2MB)
테스트 21 〉	통과 (0.61ms, 10.2MB)
테스트 22 〉	통과 (0.62ms, 10.3MB)
테스트 23 〉	통과 (1.05ms, 10.4MB)
테스트 24 〉	통과 (0.93ms, 10.4MB)
테스트 25 〉	통과 (96.60ms, 40.1MB)
테스트 26 〉	통과 (111.53ms, 40.7MB)
테스트 27 〉	통과 (119.20ms, 43.7MB)
테스트 28 〉	통과 (111.97ms, 45.3MB)
테스트 29 〉	통과 (116.88ms, 45.3MB)
테스트 30 〉	통과 (81.98ms, 37.6MB)
테스트 31 〉	통과 (95.87ms, 44.2MB)
테스트 32 〉	통과 (86.03ms, 39.9MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
"""