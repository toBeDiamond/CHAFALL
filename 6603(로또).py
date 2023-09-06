def comb(n, r, k, s): # s는 시작 숫자
    if r == k:
        print(*p)
    else:
        for i in range(s, n - r + 1 + k): # n - r + 1 :선택할 수 있는 마지막 원소
            p[k] = S[i]
            comb(n, r, k+1, i+1)

N = 6
while True:
    K, *S = list(map(int, input().split()))
    p = [0] * N
    comb(K, N, 0, 0)
    print()
    if K == 0:
        break

