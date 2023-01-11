from string import ascii_uppercase

def solution(msg):
    answer = []
    index_dict = {val: idx+1 for idx, val in enumerate(ascii_uppercase)}
    pressed = ""
    end_idx = len(ascii_uppercase) + 1
    idx = 0

    while idx < len(msg):
        pressed += msg[idx]

        if pressed in index_dict:
            idx += 1
            continue
        else:
            index_dict[pressed] = end_idx
            end_idx += 1

            answer.append(index_dict[pressed[:-1]])
            pressed = ''

    answer.append(index_dict[pressed])

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))