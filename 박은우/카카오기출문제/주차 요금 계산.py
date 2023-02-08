import math


# fees: [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
def get_fee(minutes, fees):
    return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]


def solution(fees, records):
    print('-------------------------')
    stack = dict()
    parking = dict()

    for record in records:
        time, car, event = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)  # 시간 -> 분 환산

        if event == 'IN':
            parking[car] = minutes
        if event == 'OUT':
            try:
                stack[car] += minutes - parking[car]
                print("try car = {}, stack[car] = {}, parking[car] = {}".format(car, stack[car], parking[car]))
            except:
                stack[car] = minutes - parking[car]
                print("except car = {}, stack[car] = {}, parking[car] = {}".format(car, stack[car], parking[car]))
            del parking[car]  # 출차 차량 삭제

    print('parking.items() = {}'.format(parking.items()))
    # 출차 기록 없는 차 23:59 출차 처리
    for car, minute in parking.items():
        try:
            stack[car] += 23 * 60 + 59 - minute
        except:
            stack[car] = 23 * 60 + 59 - minute

    print('stack.items() = {}'.format(stack.items()))
    return [get_fee(time, fees) for car, time in sorted(list(stack.items()), key=lambda x: x[0])]


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10],
               ["00:00 1234 IN"]))

"""
fees의 길이 = 4

fees[0] = 기본 시간(분)
1 ≤ fees[0] ≤ 1,439
fees[1] = 기본 요금(원)
0 ≤ fees[1] ≤ 100,000
fees[2] = 단위 시간(분)
1 ≤ fees[2] ≤ 1,439
fees[3] = 단위 요금(원)
1 ≤ fees[3] ≤ 10,000

1 ≤ records의 길이 ≤ 1,000

records의 각 원소는 "시각 차량번호 내역" 형식의 문자열입니다.
시각, 차량번호, 내역은 하나의 공백으로 구분되어 있습니다.
시각은 차량이 입차되거나 출차된 시각을 나타내며, HH:MM 형식의 길이 5인 문자열입니다.
HH:MM은 00:00부터 23:59까지 주어집니다.
잘못된 시각("25:22", "09:65" 등)은 입력으로 주어지지 않습니다.
차량번호는 자동차를 구분하기 위한, `0'~'9'로 구성된 길이 4인 문자열입니다.
내역은 길이 2 또는 3인 문자열로, IN 또는 OUT입니다. IN은 입차를, OUT은 출차를 의미합니다.
records의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어집니다.
records는 하루 동안의 입/출차된 기록만 담고 있으며, 입차된 차량이 다음날 출차되는 경우는 입력으로 주어지지 않습니다.
같은 시각에, 같은 차량번호의 내역이 2번 이상 나타내지 않습니다.
마지막 시각(23:59)에 입차되는 경우는 입력으로 주어지지 않습니다.
아래의 예를 포함하여, 잘못된 입력은 주어지지 않습니다.
주차장에 없는 차량이 출차되는 경우
주차장에 이미 있는 차량(차량번호가 같은 차량)이 다시 입차되는 경우
"""


def solution(fees, records):
    parking = dict()
    stack = dict()

    for record in records:
        time, car, cmd = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)  # 시간 -> 분 환산

        if cmd == 'IN':
            parking[car] = minutes
        elif cmd == 'OUT':
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car]  # 출차 차량 삭제

    # 출차 기록 없는 차 23:59 출차 처리
    for car, minute in parking.items():
        try:
            stack[car] += 23 * 60 + 59 - minute
        except:
            stack[car] = 23 * 60 + 59 - minute

    return [get_fee(time, fees) for car, time in sorted(list(stack.items()), key=lambda x: x[0])]