# DP의 냄새가 난다.

def solution(n):

    dp = [1] + [1] + [2] + [0] * (n - 2)

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]


    return dp[n] % 1234567

print(solution(4))