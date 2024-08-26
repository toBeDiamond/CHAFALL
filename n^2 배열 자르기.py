# 시간 초과 코드
def solution(n, left, right):
    arr = [[False]  * n for _ in range(n)]

    # 배열 값 넣기
    # for k in range(1, n + 1):
    #     for i in range(k):
    #         for j in range(k):
    #             if not arr[i][j]:
    #                 arr[i][j] = k

    # 각 숫자로 배열을 채움
    for k in range(1, n + 1):
        # 이중 반복문을 돌리기 전에, 이미 채워진 부분을 피할 수 있도록 배열을 채움
        for i in range(k - 1, k):
            for j in range(k):
                arr[i][j] = k
                arr[j][i] = k

    # 1차원 배열로
    one = []
    for a in arr:
        one.extend(a)

    return one[left:right + 1]

print(solution(3, 2, 5))

#------
def solution(n, left, right):

    arr = []

    for i in range(n):
        for j in range(n):
            if i <= j:
                arr.append(j + 1)
            else:
                arr.append(i + 1)

    return arr[left:right + 1]

print(solution(3, 2, 5))

# 1234 2234 3334 4444
#------
def solution(n, left, right):

    arr = []
    for i in range(left, right + 1):
        arr.append(max(i // n, i % n) + 1)

    return arr

print(solution(3, 2, 5))