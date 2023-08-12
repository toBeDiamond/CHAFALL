M, N = map(int, input().split())

for i in range(M, N+1):
    is_prime = True
    # 1은 소수가 될 수 없다.
    if i == 1:
        is_prime = False
    else:
        # 해당 숫자 앞의 숫자들로 나누어 줌
        for j in range(2, int(i**0.5+1)):
            if i % j == 0:
                is_prime = False
                break
    # for문 안에서 print를 해주면 중복해서 계속 나오므로 bool 사용
    if is_prime:
        print(i)