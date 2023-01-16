from collections import defaultdict
from math import ceil
LAST_TIME = 23*60 + 59

def exchange_mins(rec_time):
    hour, mins = map(int, rec_time.split(':'))
    return hour*60 + mins

def get_parking_fee(mins, fees):
    if mins <= fees[0]:
        return fees[1]
    else:
        over_time = mins - fees[0]
        over_time = int(ceil(over_time / fees[2]))
        return fees[1] + over_time * fees[-1]

def solution(fees, records):
    answer = []
    in_time = defaultdict(int)
    total_time = defaultdict(int)

    for record in records:
        rec_split = record.split() #시간, 차번호, 입출차
        car = rec_split[1]

        if rec_split[-1] == 'IN':
            in_time[car] = exchange_mins(rec_split[0])
        elif rec_split[-1] == 'OUT':
            out_mins = exchange_mins(rec_split[0])
            total_time[car] += (out_mins - in_time[car])
            in_time[car] = -1

    for car in in_time.keys():
        if in_time[car] != -1:
            total_time[car] += (LAST_TIME - in_time[car])
    ordered_car = sorted(total_time.keys())

    for car in ordered_car:
        answer.append(get_parking_fee(total_time[car], fees))

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))