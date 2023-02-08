def convert(n, base):
    base_str = '0123456789ABCDEF'
    q, r = divmod(n, base)

    if q == 0:
        return base_str[r]
    else:
        return convert(q, base) + base_str[r]


def solution(n, t, m, p):
    needed_num = ''
    answer = ''

    for i in range(m*t):
        needed_num += convert(i, n)

    answer = needed_num[p-1:m*t:m]

    return answer