# N = int(input())
# arr = list((map(int, input().split())))
# x = int(input())
#
# real_counts = 0
# for i in range(1<<N): #2^n
#     counts = 0
#     total = 0
#     for j in range(N):
#         if i & (1<<j):
#             counts += 1
#             total += arr[j]
#     if counts == 2 and total == x:
#         real_counts += 1
#
# print(real_counts)
#
# #-------------------------------------------------------
# N = int(input())
# arr = list((map(int, input().split())))
# x = int(input())
#
# arr = sorted(arr)
# counts = 0
# for i in range(N):
#     for j in range(i+1, N):
#         if arr[i] + arr[j] == x:
#             counts += 1
#             break
#         elif arr[i] + arr[j] > x:
#             break
#
# print(counts)
#--------------------------------------------------------
N = int(input())
arr = list((map(int, input().split())))
x = int(input())
arr.sort()

i = 0 # 최솟값
j = N-1 # 최댓값
counts = 0
while i < j:
    # 두 원소의 합이 x와 같으면 카운트
    if arr[i] + arr[j] == x:
        counts += 1
    # 여기서 인지해야 할 것은 두 원소의 합이 x와 같을 때도
    # 인덱스 조정이 있어야 한다는 점이다.
    # 그냥 아래의 if문에서 같을 때엔 최댓값 인덱스 1 감소하는 것으로 퉁침

    # 두 원소의 합이 x보다 크면 최댓값 인덱스 1 감소
    if arr[i] + arr[j] >= x:
        j -= 1
    # 두 원소의 합이 x보다 작을 때
    else:
        i += 1

print(counts)