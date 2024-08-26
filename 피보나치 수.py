# 시간 초과 발생 (재귀)
# def solution(n):
#     if n < 2:
#         return n
#     else:
#         return (solution(n - 1) + solution(n -2)) %1234567


def solution(n):
    ans = [0, 1]
    for i in range(2, n + 1):
        ans.append((ans[i - 1] + ans[i - 2]) %1234567)

    return ans[-1]

print(solution(5))
