# 일단 방문체크가 있어야 될까? 딴 길로 왔는데 더 빠른 루트였다면?
# 다른 느낌의 방문체크가 있어야 될 듯
# 방향 전환 오랜만에 ㄱ?
# BFS?

# from collections import deque
#
# # 우 하 좌 상
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# def bfs(board):
#     N = len(board)
#     # 방문 시에 비용이 얼마나 들었나 체크할 배열
#     # 같을 시에도 갱신해줄 것!! (그래야 멈추지 않고 계속 진행)
#     cost = [[987654321] * N for _ in range(N)]
#     # 시작 지점
#     cost[0][0] = 0
#
#     Q = deque()
#     # 방향을 9로 한 이유는 시각지점에서 오른쪽과 아래쪽 둘 다 드는 비용이 100으로 고정하기 위함
#     Q.append((0, 0, 0, 9))  # 좌표 i, j, 비용, 방향
#
#     while Q:
#         i, j, c, dir = Q.popleft()
#
#         if i == N - 1 and j == N - 1:
#             # 더 나은 루트가 있을 수 있으므로 바로 나오지 않음
#             continue
#
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#
#             # 인덱스 조건
#             if 0 <= ni < N and 0 <= nj < N:
#                 # 벽이면 다른 방향 찾기
#                 if board[ni][nj] == 1:
#                     continue
#                 # 비용 관련
#                 # 만약에 첫 스타트거나 방향 변화가 없으면
#                 if dir == 9 or dir == k:
#                     nc = c + 100
#                 else:
#                     nc = c + 600
#
#                 # 비용이 작거나 같으면 갱신하고 Q에 넣어주기(넌 갈만한 애야)
#                 if nc <= cost[ni][nj]:
#                     cost[ni][nj] = nc
#                     Q.append((ni, nj, nc, k))
#
#     return cost[N - 1][N - 1]
#
#
# def solution(board):
#
#     return bfs(board)
# #
# # print(solution([[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 0, 1, 0, 0],[1, 0, 0, 0, 1],[1, 1, 1, 0, 0]]))
#
# # 이 문제는 단순히 그 위치에서의 최소 비용을 저장하면 안되고 그 위치에서 방향별 최소비용을 저장할 수 있도록 해야합니다.
# # 방향이 비용에 영향을 끼치기 때문입니다.
#
# # dfs는 한 경로를 끝까지 쭉 가보는 반면 bfs는 모든 경웅의 수에 대해서 depth를 하나씩 늘려가면서 진행하죠.
# # 이 문제의 경우 현재까지의 코스트가 최소라고 해도
# # 다음번에 꺾이느냐 안꺾이느냐에 따라서 최적 경로와 코스트가 달라지므로 기본적인 dfs 방법으로는 풀기 힘들겠네요.
#
#
# from collections import deque
#
# # 우 하 좌 상
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# def bfs(board):
#     N = len(board)
#     # 방문 시에 비용이 얼마나 들었나 체크할 배열
#     # 3차원으로 변경
#     cost = [[[987654321] * N for _ in range(N)] for _ in range(4)]
#
#     # 시작 지점 초기화
#     for p in range(4):
#         cost[p][0][0] = 0
#
#
#     # 한칸씩 이동한 후로 생각 (처음엔 방향 신경 x)
#     Q = deque()
#
#     # 오른쪽
#     if board[0][1] != 1:
#         Q.append((0, 1, 100, 0))  # 좌표 i, j, 비용, 방향
#         cost[0][0][1] = 100
#     # 아래
#     if board[1][0] != 1:
#         Q.append((1, 0, 100, 1))  # 좌표 i, j, 비용, 방향
#         cost[1][1][0] = 100
#
#
#     while Q:
#         i, j, c, dir = Q.popleft()
#
#         if i == N - 1 and j == N - 1:
#             # 더 나은 루트가 있을 수 있으므로 바로 나오지 않음
#             continue
#
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#
#             # 인덱스 조건
#             if 0 <= ni < N and 0 <= nj < N:
#                 # 벽이면 다른 방향 찾기
#                 if board[ni][nj] == 1:
#                     continue
#                 # 비용 관련
#                 # 방향 변화가 없으면
#                 if dir == k:
#                     nc = c + 100
#                 else:
#                     nc = c + 600
#
#                 # 비용이 작거나 같으면 갱신하고 Q에 넣어주기(넌 갈만한 애야)
#                 if nc < cost[k][ni][nj]:
#                     cost[k][ni][nj] = nc
#                     Q.append((ni, nj, nc, k))
#
#     ans = 987654321
#     for p in range(4):
#         ans = min(ans, cost[p][N - 1][N - 1])
#
#     return ans
#
#
# def solution(board):
#
#     return bfs(board)
#
# print(solution([[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 0, 1, 0, 0],[1, 0, 0, 0, 1],[1, 1, 1, 0, 0]]))

import heapq

# 이동 방향을 나타내는 배열 (상, 하, 좌, 우)
my = [1, -1, 0, 0]
mx = [0, 0, 1, -1]


def solution(board):
    INF = 1e10  # 무한대를 나타내는 값
    n = len(board)  # 보드의 크기

    # 비용을 저장하는 3차원 리스트 (각 위치에서 방향별로 최소 비용을 저장)
    cost = [[[INF] * 2 for _ in range(n)] for _ in range(n)]

    # 우선순위 큐 (최소 힙) 초기화
    q = []

    # 시작점 (0, 0)에서 출발, 초기 비용은 0, 초기 방향은 -1 (미정)
    heapq.heappush(q, (0, 0, 0, -1))

    while q:
        # 큐에서 비용, 현재 위치 (y, x), 방향 (d)을 꺼냄
        c, y, x, d = heapq.heappop(q)
        print(cost[y][x][d],c)


        # 이미 현재 비용보다 작은 비용이 있으면 건너뜀
        if d != -1 and cost[y][x][d] < c:
            continue

        # 4 방향으로 이동
        for i in range(4):
            dy = y + my[i]
            dx = x + mx[i]
            new_d = 0 if i >= 2 else 1  # i가 2 또는 3이면 좌우 이동 (가로), 아니면 상하 이동 (세로)

            # 경계를 넘지 않고 벽이 아닌 경우
            if 0 <= dy < n and 0 <= dx < n and not board[dy][dx]:

                # 초기 위치 (0, 0)에서 다른 위치로 가는 경우
                if d == -1:
                    new_cost = 100  # 초기 비용 100
                    cost[dy][dx][new_d] = new_cost
                    heapq.heappush(q, (new_cost, dy, dx, new_d))
                else:
                    # 같은 방향으로 이동하면 100원, 다른 방향으로 이동하면 600원 (회전 비용 포함)
                    new_cost = c + 100 if d == new_d else c + 600
                    if cost[dy][dx][new_d] > new_cost:
                        cost[dy][dx][new_d] = new_cost
                        heapq.heappush(q, (new_cost, dy, dx, new_d))

    # 최종 목적지 (n-1, n-1)의 최소 비용 반환
    return min(cost[n - 1][n - 1])


# 예시 실행
# board = [
#     [0, 0, 0],
#     [1, 0, 1],
#     [0, 0, 0]
# ]
print(solution([[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 0, 1, 0, 0],[1, 0, 0, 0, 1],[1, 1, 1, 0, 0]]))