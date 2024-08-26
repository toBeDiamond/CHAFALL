def solution(A,B):
    answer = 0

    # 하나는 오름차순, 다른 하나는 내림차순으로 처리해서
    # 곱해주면 됨

    N = len(A)

    A.sort()
    B.sort(reverse=True)

    for i in range(N):
        answer += A[i] * B[i]

    return answer

print(solution([1, 4, 2], [5, 4, 4]	))