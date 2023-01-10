def solution(N, number):

    if number == N:
        return 1

    answer = -1

    set_array = [set() for i in range(8)]
    print(set_array)

    # 1  2   3    4     5      6       7        8
    # 5 55 555 5555 55555 555555 5555555 55555555
    for i in range(len(set_array)):
        set_array[i].add(int(str(N) * (i+1)))

    print(set_array)

    for i in range(1, 8):
        for j in range(i):
            for op1 in set_array[j]:
                for op2 in set_array[i - j - 1]:
                    # print('------')
                    # print('[INFO] now set_array[i] = {}'.format(set_array[i]))
                    set_array[i].add(op1 + op2)
                    set_array[i].add(op1 - op2)
                    set_array[i].add(op1 * op2)
                    if op2 != 0:
                        set_array[i].add(op1 // op2)
                    # print('[DEBUG] i = {}, j = {}, op1 = {}, op2 = {}, set_array[i] = {}'.format(i, j, op1, op2, set_array[i]))

        if number in set_array[i]:
            answer = i+1
            break

    print(set_array)
    return answer

print(solution(5, 12))
print(solution(2, 11))