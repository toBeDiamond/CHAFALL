# def bfs(p, q):
#     o = v = 0
#     Q = []
#     Q.append((p, q))
#     visited[p][q] = 1
#
#     while Q:
#         i, j = Q.pop(0)
#         if arr[i][j] == 'o':
#             o += 1
#         elif arr[i][j] == 'v':
#             v += 1
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0\
#                 and arr[ni][nj] != '#':
#                 # 양이면
#                 if arr[ni][nj] == 'o':
#                     o += 1
#                 # 늑대이면
#                 elif arr[ni][nj] == 'v':
#                     v += 1
#                 Q.append((ni, nj))
#                 visited[ni][nj] = 1
#
#     return o, v
#
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# # .: 빈칸, #: 울타리, o: 양, v: 늑대
# R, C = map(int, input().split())
# arr = [list(input()) for _ in range(R)]
# visited = [[0] * C for _ in range(R)]
#
# o_num = v_num = 0
# for i in range(R):
#     for j in range(C):
#         if visited[i][j] == 0 and (arr[i][j] =='o' or arr[i][j] == 'v'):
#             o, v = bfs(i, j)
#             if o > v:
#                 o_num += o
#             else:
#                 v_num += v
#
# print(o_num, v_num)

#-------------------------------------------------------------------
def bfs(p, q):
    o = v = 0
    Q = []
    Q.append((p, q))
    visited[p][q] = 1
    if arr[p][q] == 'o':
        o += 1
    elif arr[p][q] == 'v':
        v += 1

    while Q:
        i, j = Q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0\
                and arr[ni][nj] != '#':
                # 양이면
                if arr[ni][nj] == 'o':
                    o += 1
                # 늑대이면
                elif arr[ni][nj] == 'v':
                    v += 1
                Q.append((ni, nj))
                visited[ni][nj] = 1

    return o, v


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# .: 빈칸, #: 울타리, o: 양, v: 늑대
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

o_num = v_num = 0
for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and (arr[i][j] =='o' or arr[i][j] == 'v'):
            # 양이나 늑대이면 탐색 시작
            o, v = bfs(i, j)
            # 탐색하고 나오면 수 비교
            if o > v:
                o_num += o
            else:
                v_num += v

print(o_num, v_num)
