def solution(clothes):
    info = {}
    for cloth in clothes:
        info[cloth[1]] = info.setdefault(cloth[1], 0) + 1

    total = 1
    for cnt in info.values():
        total *= (cnt + 1) # 여기서 1을 더해주는 이유는 선택하지 않았을 경우를 포함하기 위함


    return total - 1 # 아무것도 선택하지 않은 경우는 빼줘야 됨.



print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))