def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.pop(0)
        # 하고 싶은 일
        if v == B:
            return visited[v] - 1 # 자기자신은 빼주기

        for w in range(1, n+1):
            if adj[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1
    return -1

n = int(input()) # 전체 사람의 수
A, B = map(int, input().split()) # 비교대상
m = int(input()) # 부모 자식들 간의 관계의 개수
visited = [0] * (n + 1)
adj = [[0] * (n + 1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())

    adj[x][y] = adj[y][x] = 1 # 인접리스트 만들기

print(bfs(A))
