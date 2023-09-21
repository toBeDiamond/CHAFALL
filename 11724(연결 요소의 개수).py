import sys
sys.setrecursionlimit(10000)
def dfs(v):
    visited[v] = 1 # 방문체크

    for w in range(1, N + 1):
        if adj[v][w] == 1 and visited[w] == 0:
            dfs(w)



N, M = map(int,sys.stdin.readline().split())
adj = [[0] * (N + 1) for _ in range(N + 1)]
visited = [1] + [0] * N # 그냥
for _ in range(M):
    s, e = map(int, input().split())
    adj[s][e] = 1 # 유방

cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
#-------------------------------------------------------
import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] * n for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)  # 방문체크


def bfs(n):
    queue = deque([n])
    while (queue):
        n = queue.popleft()
        for node in graph[n]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1


cnt = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)
