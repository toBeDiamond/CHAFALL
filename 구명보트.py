# 정렬을 한번 하고 최대한 무거운 놈은 최대한 가벼운 놈이랑 매칭 시키자
# 투 포인터 문제인 듯

def solution(people, limit):
    answer = 0
    people.sort() # 오름차순

    i = 0; j = len(people) - 1

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        # 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로
        # 사람들을 구출할 수 없는 경우는 없습니다.
        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))