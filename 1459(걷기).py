# W: 가로나 세로로 갈 때 걸리는 시간, S: 대각선으로 이동시 걸리는 시간
X, Y, W, S = map(int, input().split())
# 가로세로가 대각선 보다 이득일 때
hours = 0
if 2 * W < S:
    hours += (X + Y) * W

# 대각선이 가로세로보다 이득인 경우
else:
    temp = min(X, Y)
    if W > S:  # 대각선이 압도적으로 이득인 경우
        if (X + Y - temp * 2) % 2 == 0:
            hours += temp * S + (X + Y - temp * 2) * S
        else: # 대각선이 압도적으로 이득이라도 한칸만 남은 경우 손해
            hours += temp * S + (X + Y - temp * 2 - 1) * S + W
    else:
        hours += temp * S + (X + Y - temp * 2) * W
print(hours)
#--------------------------------------------------------------------
# W: 가로나 세로로 갈 때 걸리는 시간, S: 대각선으로 이동시 걸리는 시간
X, Y, W, S = map(int, input().split())
# 가로세로가 대각선 보다 이득일 때
hours = 0
if 2 * W < S:
    hours += (X + Y) * W

# 대각선이 가로세로보다 이득인 경우
else:
    temp = min(X, Y)
    if W > S:  # 대각선이 압도적으로 이득인 경우
        if abs(X-Y) == 0:
            hours += temp * S + abs(X - Y) * S
        else: # 대각선이 압도적으로 이득이라도 한칸만 남은 경우 손해
            hours += temp * S + (abs(X - Y) - 1) * S + W
    else:
        hours += temp * S + abs(X - Y) * W
print(hours)

# 다른 방식으론 이렇게 비용에 따른 분류 말고, 이동 방식으로 분류하고 마지막에 min으로
# 뽑아내는 방식도 있을 것이다.