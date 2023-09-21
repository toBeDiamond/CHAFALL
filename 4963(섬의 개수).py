import sys
sys.setrecursionlimit(10000)

def dfs(i, j):
    visited[i][j] = 1 # 방문 체크

    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < h and 0 <= nj < w and visited[ni][nj] == 0\
            and arr[ni][nj] == 1:
            dfs(ni, nj)

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            # 해당 조건 만족하면 탐색 시작
            if arr[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                dfs(i, j)

    print(cnt)
