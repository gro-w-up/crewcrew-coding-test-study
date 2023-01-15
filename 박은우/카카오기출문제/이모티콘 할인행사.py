def solution(users, emoticons):
    print('-------------------------')
    from itertools import product
    answer = [0, 0]
    percents = (10, 20, 30, 40)
    prod = product(percents, repeat=len(emoticons))

    for discounts in prod:
        sold = [0, 0] # 이모티콘, 판매액
        for user_discount, user_money in users:
            sold_emoticons = 0
            print('zip before emoticons = {}, discounts = {}'.format(emoticons, discounts))
            for emoticon, discount in zip(emoticons, discounts):
                print('user_discount = {}, user_money = {}, emoticon = {}, discount = {}'.format(user_discount, user_money, emoticon, discount))
                if discount >= user_discount:
                    sold_emoticons += emoticon * (1 - discount / 100)
            if sold_emoticons >= user_money:
                sold[0] += 1
            else:
                sold[1] += sold_emoticons
        answer = max(answer, sold)

    return answer

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
#solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])