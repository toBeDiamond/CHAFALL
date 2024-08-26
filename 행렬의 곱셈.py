def solution(arr1, arr2):

    # A * B 행렬 X B * C 행렬 = A * C 행렬

    R1 = len(arr1); C1 = len(arr1[0])
    R2 = len(arr2); C2 = len(arr2[0])

    answer = [[0] * C2 for _ in range(R1)]

    for k in range(R1):
        for i in range(C2):
            for j in range(C1):
                answer[k][i] += arr1[k][j] * arr2[j][i]

    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))