# 방식 1
def solution(n):
    ans = 0

    while n:
        a , b = divmod(n, 2)
        n = a
        # 나머지가 있으면 걷자
        if b == 1:
            ans += 1

    return ans

print(solution(5))

# 방식 2
def solution(n):
    ans = 0

    while n:
        if n % 2 == 0:
            n //= 2
        # 나누어 떨어지지 않으면 걷자
        else:
            ans += 1
            n -= 1

    return ans

print(solution(5))