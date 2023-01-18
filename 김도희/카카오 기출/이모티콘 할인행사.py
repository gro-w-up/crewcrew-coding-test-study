from itertools import product

def solution(users, emoticons):
    answer = [float('-inf'), float('-inf')]

    for cases in product([10, 20, 30, 40], repeat=len(emoticons)):
        subscriber, sales = 0, 0

        for wanted_discount, limit_price in users:
            purchase = 0

            for idx, case in enumerate(cases):
                if case >= wanted_discount:
                    purchase += (emoticons[idx] * (100 - case) // 100)

            if purchase >= limit_price:
                subscriber += 1
                purchase = 0

            sales += purchase

        if answer[0] < subscriber:
            answer[0] = subscriber
            answer[1] = sales

        elif answer[0] == subscriber:
            answer[1] = max(answer[1], sales)

    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))