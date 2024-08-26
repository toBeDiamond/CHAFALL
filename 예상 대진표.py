def solution(n,a,b):
    answer = 0

    while a != b:
        answer += 1
        # 나누어 떨어지는 경우를 고려
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)

    return answer

print(solution(8, 4, 7))

# while로??
# [1 2] [3 4] [5 6] [7 8]
# [1 4] [5 7]
# [4 7]
# 리스트의 갯수만 안다면 몇 라운드인지는 그냥 알 수 있음