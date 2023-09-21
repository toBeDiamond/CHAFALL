# N = int(input())
# arr = list(map(int, input().split()))
# C = [0] * N
# for i in range(N):
#     k = 0
#     while C[arr[i] + k] != 0:
#         k += 1
#     C[arr[i] + k] = i + 1
#
#
# print(*C)
#------------------------------------------------

N = int(input())
arr = list(map(int, input().split()))
C = [0] * N
for i in range(N):
    cnt = 0
    j = 0
    # 내 앞에 나 보다 큰 놈(0)이 있을 자리 입력에 맞게 비워두기
    while cnt < arr[i]:
        if C[j] == 0:
            cnt += 1
        j += 1
    # 나보다 작은 놈이 내가 있어도 되는 자리를 차지하고 있으면 작은놈보단 뒤에 자리잡기
    while C[j] != 0:
        j += 1
    C[j] = i + 1

print(*C)

