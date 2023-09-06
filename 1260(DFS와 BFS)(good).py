def dfs(v):
    visited[v] = 1  # 방문체크
    print(v, end=' ')  # 할 일

    for w in range(1, N + 1):
        if visited[w] == 0 and adj[v][w] == 1:
            dfs(w)


def bfs(v):
    Q = []
    Q.append(v)
    visited2[v] = 1  # 방문체크
    print(v, end=' ')  # 할 일

    while Q:
        v = Q.pop(0)
        for w in range(1, N + 1):
            if visited2[w] == 0 and adj[v][w] == 1:
                Q.append(w)
                visited2[w] = 1
                print(w, end=' ')  # 할 일


# N 정점의 개수 M 간선의 개수 V 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())
visited = [0] * (N + 1)
visited2 = [0] * (N + 1)
adj = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    s, e = map(int, input().split())
    adj[s][e] = adj[e][s] = 1

dfs(V)
print()
bfs(V)
