Round = int(input())
for r in range(1, Round+1):
    A_num, *A_list = map(int, input().split()) # 언패킹 써보기
    B_num, *B_list = map(int, input().split())

    A_list.sort(reverse = True)
    B_list.sort(reverse = True)

    i = 0
    while i < A_num and i < B_num:
        if A_list[i] > B_list[i]:
            print('A')
            break
        elif A_list[i] < B_list[i]:
            print('B')
            break
        elif A_list[i] == B_list[i]:
            i += 1
    else:
        if A_num == B_num:
            print('D')
        elif A_num > B_num:
            print('A')
        elif A_num < B_num:
            print('B')


