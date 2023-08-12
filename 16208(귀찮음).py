N = int(input())
stick = list(map(int, input().split()))
stick.sort()
remain_stick = sum(stick)

ans = 0
for i in stick:
    remain_stick -= i
    ans += remain_stick * i

print(ans)

# 큰거 곱하기 큰거 보단 큰거 곱하기 작은것을 할 때가 더 최소에...

