# N = int(input())
# N_list = list(map(int, input().split()))
# M = int(input())
# M_list = list(map(int, input().split()))
#
# for m in M_list:
#     is_number = False
#     if m in N_list:
#         is_number = True
#
#     if is_number:
#         print(1)
#     else:
#         print(0)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

def findnumber(a, n, key):
    start = 0
    end = n-1
    while start <= end:
        mid = (start + end) // 2
        # 검색 성공
        if a[mid] == key:
            return 1
        # 더 작은 값에서 찾아봐
        elif a[mid] > key:
            end = mid - 1
        # 더 큰 값에서 찾아봐
        else:
            start = mid + 1
    # 없으면...
    return 0

arr = sorted(N_list) # 이진탐색은 정렬이 필수!
for key in M_list:
    print(findnumber(arr, len(arr), key))






