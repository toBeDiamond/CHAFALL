num = input()
N = len(num)
counts = 1
for i in range(1, N):
    if num[i-1] != num[i]:
        counts+=1

print(counts // 2)