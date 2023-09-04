# 최소 한 개의 모음과 최소 2개의 자음
def comb(n, r, k, s): # s는 시작 숫자
    if r == k:
        cnt = 0
        for p_i in p:
            if p_i in 'aeiou':
                cnt += 1
        if 1 <= cnt <= L - 2:
            print(''.join(p))
    else:
        for i in range(s, n - r + 1 + k): # n - r + 1 :선택할 수 있는 마지막 원소
            p[k] = arr[i]
            comb(n, r, k+1, i+1)

L, C = map(int, input().split())
arr = input().split()
arr.sort()

p = [0] * L
comb(C, L, 0, 0)

