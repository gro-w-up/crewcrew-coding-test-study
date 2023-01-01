from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    answer = 0
    cashe = deque()

    for city in cities:
        city = city.lower()

        if city not in cashe:  # cashe miss
            if len(cashe) == cacheSize:
                # if cashe is fulled, first cashe is deleted
                cashe.popleft()
            cashe.append(city)
            answer += 5
        else:  # cashe hit
            cashe.remove(city)
            cashe.append(city)
            answer += 1
    return answer