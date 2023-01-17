import math


def convert(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)


def solution(fees, records):
    intime = {}
    result = {}

    for val in records:
        time, num, inout = val.split()
        if inout == 'IN':
            intime[num] = convert(time)
            if num not in result:
                result[num] = 0
        else:
            result[num] += convert(time) - intime[num]
            del intime[num]

    for idx, val in intime.items():
        result[idx] += 23 * 60 + 59 - val

    answer = []
    for idx, val in sorted(result.items()):
        if val <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((val - fees[0]) / fees[2]) * fees[3])
    return answer


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
