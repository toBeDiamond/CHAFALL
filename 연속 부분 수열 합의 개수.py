def solution(elements):
    N = len(elements)
    # 원형을 선형으로
    elements = elements + elements[:-1]
    sum_info = set()

    for i in range(1, N + 1): # size
        for j in range(N):
            sum_info.add(sum(elements[j : j + i]))

    return len(sum_info)

print(solution([7,9,1,1,4]))