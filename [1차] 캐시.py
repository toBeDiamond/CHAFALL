from collections import deque

def solution(cacheSize, cities):
    answer = 0

    cache = deque()
    cnt = 0 # 매번 len 하지 않기 위해
    # 예외 조건
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.upper() # 대문자로 통일

        # 캐시 안에 있는 경우
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            # 빈 자리가 있다면
            if cnt < cacheSize:
                cache.append(city)
                cnt += 1
            else:
                cache.popleft()
                cache.append(city)
            answer += 5

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))