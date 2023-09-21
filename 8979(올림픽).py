N, K = map(int, input().split())

arr = []
# 국가, 금, 은 ,동
for _ in range(N):
    k, g, s, b = map(int, input().split())
    # 순위 알고 싶은 나라 따로 빼놓기 (대한민국이라고 생각하겠음)
    if k != K:
        arr.append([g, s, b])
    else:
        korea = [g, s, b]

rank = 1  # 초기 상태
for i in range(N - 1): # 우리나라 빼놨으므로
    # 금메달이 더 많은 나라 있으면 순위 하나 미루기
    if korea[0] < arr[i][0]:
        rank += 1
    # 금메달 수 같고, 은메달 수 더 많은 나라 있으면 순위 미루기
    elif korea[0] == arr[i][0] and korea[1] < arr[i][1]:
        rank += 1
    # 금,은메달수 같고, 동메달 수 더 많은 나라 있으면 순위 미루기
    elif korea[0] == arr[i][0] and korea[1] == arr[i][1]\
            and korea[2] < arr[i][2]:
        rank += 1

print(rank)



