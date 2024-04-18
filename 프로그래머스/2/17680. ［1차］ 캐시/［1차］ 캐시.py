def solution(cacheSize, cities):
    answer = 0
    cache_miss = 5
    cache_hit = 1
    cache = []
    if cacheSize==0: 
        return len(cities)*cache_miss
    
    for city in cities:
        city = city.lower()
        if not city in cache:
            if len(cache) < cacheSize:
                cache.append(city)
                answer+=cache_miss
            elif len(cache) == cacheSize:
                cache.pop(0)
                cache.append(city)
                answer+=cache_miss
        elif city in cache:
            cache.pop(cache.index(city))
            cache.append(city)
            answer+=cache_hit
    return answer
