def dfs(v):
    visited[v] = 1
    for w in range(1, V+1):
        if visited[w] == 0 and adj[v][w] == 1:
            dfs(w)



V = int(input())
E = int(input())
adj = [[0] * (V + 1) for _ in range(V+1)]
visited = [0] * (V + 1)
for i in range(E):
    s, e = map(int, input().split())
    adj[s][e] = adj[e][s] = 1

dfs(1)

print(visited.count(1) - 1)
