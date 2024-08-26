N = 0
answer = 0
visited = []

def dfs(k, cnt, dungeons): # 남은 피로도, 돈 던전 수, 던전
    global answer
    # 갱신 조건
    if answer < cnt:
        answer = cnt

    for i in range(N):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = 0  # 원상복구

    return

def solution(k, dungeons):
    global N, visited

    N = len(dungeons)  # 던전 수
    visited = [0] * N

    dfs(k, 0, dungeons)

    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))

# 피로도 순으로 하려고 했는데 높은 피로도일 때만 가능한 경우를 고려 불가
# 1~ 8? 완전탐색도 가능.
