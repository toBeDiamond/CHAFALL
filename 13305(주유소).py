N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))


# 초기설정 (맨 첫 놈은 무조건 최소 첫 거리를 갈 만큼의 기름을 넣어야 한다.)
cost = distance[0] * price[0]

min_price = price[0]
for i in range(1, N-1): # 마지막 놈의 price는 신경 x
    if min_price > price[i]: # 현재 가장 싼 비용으로 더 싼 비용을 만나기 전까지는
        min_price = price[i] # 계속 그 비용으로 주유한다고 생각

    cost += min_price * distance[i]

print(cost)


