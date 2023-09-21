N, G = map(int, input().split())
arr = []
# [출발, 도착, 지름길]
for _ in range(N):
    s, e, f = map(int, input().split())
    # 지름길이 더 먼 경우와, 목적지보다 도착지가 먼 경우를 제외하고 넣어주기
    if (e - s) > f and e < G:
        arr.append([s, e, f])


