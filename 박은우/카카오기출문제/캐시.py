def solution(cache_size, cities):
    # 빈 캐시 배열 생성
    cache = []
    # 시간 체크할 변수 생성
    time = 0
    for city in cities:
        city = city.lower()

        if cache_size != 0:
            print('cache = {}'.format(cache), end=' ')
            if not city in cache:
                # cache miss
                if len(cache) == cache_size:
                    cache.pop(0)
                cache.append(city)
                time += 5
                print('time = {} (+5)'.format(time))
            else:
                # cache hit
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
                print('time = {} (+1)'.format(time))
        else:
            # cache miss
            time += 5
    return time

# expect 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# 21
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# 60
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# 52
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# 16
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
# 25
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))

"""

cache(캐시) = 컴퓨터 과학에서 데이터나 값을 미리 복사해 놓는 임시 장소

- cache라는 빈 배열을 만든다.
- .lower(): city는 대소문자를 구별하지 않으므로 for문을 돌며 cache 배열에 접근할 때 모두 소문자로 변경하여 저장한다.
- cache_size가 0인 경우에는 cache에 저장이 불가능 하므로 cache miss만 발생하여 매번 실행 시간이 5초가 되어 time에 5를 계속 더해준다.
- cache_size가 1 이상인 경우, cache hit인지 cache miss인지 판별을 해야 하므로 cache에 city가 존재하는지 확인해야 한다.
- cache miss인 경우, 먼저 cache_size와 cache의 길이가 같은 지 확인한다. 만약 같다면 더 이상 cache에 저장할 용량이 없다는 뜻으로 cache.pop(0)으로 cache의 첫 번째 값을 제거한다. 이후, cache에 cache.append(city)로 city를 저장한다. 실행 시간은 5초이므로 time에 5를 더한다.
- cache hit인 경우, 이전에 같은 이름의 city가 존재하므로 이는 가장 최근에 참조 되었다는 의미가 되므로 cache에 있던 city를 삭제한 뒤, 맨 뒤에 city를 다시 저장한다. 실행 시간은 1초이므로 time에 1을 더한다.
"""