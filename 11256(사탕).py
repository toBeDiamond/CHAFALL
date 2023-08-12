T = int(input())
for tc in range(1, T+1):
    J, N = map(int, input().split())

    Max_candy = []
    for _ in range(N):
        A, B = map(int, input().split())
        Max_candy.append(A * B)

    Max_candy.sort(reverse= True) # 내림차순
    i = 0
    while J > 0:
        J -= Max_candy[i]
        i += 1

    print(i)


