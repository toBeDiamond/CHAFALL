import sys
sys.setrecursionlimit(10000)

def dfs(i, j, k):
    visited[i][j] = 1   # 방문체크

    for p in range(4):
        ni = i + di[p]
        nj = j + dj[p]
        if 0<= ni < N and 0 <= nj < N\
                and visited[ni][nj] == 0 and arr[ni][nj] > k:
            dfs(ni, nj, k)


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_v = 1 # 이거 왜 1로 해야지 맞냐??
for k in range(1, 101):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and visited[i][j] == 0:
                dfs(i, j, k)
                cnt += 1
    if max_v < cnt:
        max_v = cnt

print(max_v)