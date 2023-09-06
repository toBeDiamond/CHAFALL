M = 5 # 카드 수
N = int(input())
max_v = 0
max_num = 0
for n in range(1, N+1):
    arr = list(map(int, input().split()))

    for i in range(M - 2):
        for j in range(i + 1, M - 1):
            for k in range(j + 1, M):
                temp = (arr[i] + arr[j] + arr[k]) % 10
                if max_v <= temp:
                    max_v = temp
                    max_num = n

print(max_num)


