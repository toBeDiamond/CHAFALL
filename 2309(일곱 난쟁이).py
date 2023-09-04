# 경우의 수 : 9C2
def find():
    for i in range(1 << 9):  # 2^12
        counts = 0
        total = 0
        ans = []
        for j in range(9):
            if i & (1 << j):
                counts += 1
                total += arr[j]
                ans.append(arr[j])
        if counts == 7 and total == 100:
            return ans

N = 9
M = 7
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
ans = find()
for i in range(7):
    print(ans[i])

#===============================================================
N = 9
M = 7
arr = []
for _ in range(N):
    arr.append(int(input()))

total = sum(arr)
for i in range(9):
    for j in range(i+1, 9):
        if total - arr[i] - arr[j] == 100:
            remove_i, remove_j = i, j
            break

arr.pop(remove_j)
arr.pop(remove_i)
arr.sort()

for i in range(7):
    print(arr[i])



