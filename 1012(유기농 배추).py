import sys
sys.setrecursionlimit(10000)

def dfs(i, j):
    visited[i][j] = 1 # 방문체크

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0\
            and arr[ni][nj] == 1:

            dfs(ni, nj)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())  # 가로, 세로 길이(열, 행 길이), 배추가 심어진 위치의 수
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())  # 열, 행
        arr[r][c] = 1  # 배추 위치 설정

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)

#-----------------------------------------------------------------------------
# def dfs(i, j):
#     arr[i][j] = 0
#
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0 <= ni < N and 0 <= nj < M \
#             and arr[ni][nj] == 1:
#
#             dfs(ni, nj)
#
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# T = int(input())
# for tc in range(1, T+1):
#     M, N, K = map(int, input().split())  # 가로, 세로 길이(열, 행 길이), 배추가 심어진 위치의 수
#     arr = [[0] * M for _ in range(N)]
#     for _ in range(K):
#         c, r = map(int, input().split())  # 열, 행
#         arr[r][c] = 1  # 배추 위치 설정
#
#     cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 1:
#                 dfs(i, j)
#                 cnt += 1
#     print(cnt)