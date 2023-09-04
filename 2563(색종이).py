N = 100
M = 10
T = int(input())

arr = [[0] * N for _ in range(N)]
for tc in range(1, T+1):
    c, r = map(int, input().split())

    for i in range(r, r+M):
        for j in range(c, c+M):
            arr[i][j] += 1

ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            ans += 1

print(ans)

