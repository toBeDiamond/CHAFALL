N = 5
arr1 = [list(map(int, input().split())) for _ in range(N)]
# 1차원으로 받기
arr2 = []
for _ in range(N):
    arr2.extend(list(map(int, input().split())))

# 부른 숫자 B로 바꾸기
for k in range(N**2):
    for i in range(N):
        for j in range(N):
            if arr1[i][j] == arr2[k]:
                arr1[i][j] = 'B'
                break


    # 행
    counts = 0
    for i in range(N):
        flag = 1
        for j in range(N):
            if arr1[i][j] != 'B':
                flag = 0
                break
        if flag == 1:
            counts += 1
    # 열
    for j in range(N):
        flag = 1
        for i in range(N):
            if arr1[i][j] != 'B':
                flag = 0
                break
        if flag == 1:
            counts += 1
    # 대각선(왼오)
    flag = 1
    for i in range(N):
        if arr1[i][i] != 'B':
                flag = 0
                break
    if flag == 1:
        counts += 1
    # 대각선(오왼)
    flag = 1
    for i in range(N):
        if arr1[i][N-1-i] != 'B':
            flag = 0
            break
    if flag == 1:
        counts += 1

    if counts >= 3:
        print(k+1) #부르는 값이 인덱스 0부터 시작하므로 1더해줌
        break

