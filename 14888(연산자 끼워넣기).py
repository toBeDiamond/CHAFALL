# 순열
def perm(N, k, op):
    global min_v, max_v
    if N == k:
        # 여기 부분 수정
        temp = arr[0]
        for i in range(N):
            if op[i] == '+':
                temp += arr[i+1]
            elif op[i] == '-':
                temp -= arr[i+1]
            elif op[i] == '*':
                temp *= arr[i+1]
            elif op[i] == '/':
                if temp < 0:
                    temp = -((-temp) // arr[i+1])
                else:
                    temp //= arr[i+1]
        if min_v > temp:
            min_v = temp
        if max_v < temp:
            max_v = temp
        return
    else:
        for i in range(k, N):
            op[k], op[i] = op[i], op[k]
            perm(N, k + 1, op)
            op[k], op[i] = op[i], op[k]

N = int(input())
M = N - 1
arr = list(map(int, input().split()))
op_arr = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = []
min_v = 9999999999
max_v = -9999999999
for i in range(4):
    for j in range(op_arr[i]):
        op.append(op_list[i])

perm(M, 0, op)
print(max_v)
print(min_v)

#---------------------------------------------------------------------
# 백트래킹
def dfs(k, temp, plus, minus, mul, div):
    global min_v, max_v

    if k == N:
        if min_v > temp:
            min_v = temp
        if max_v < temp:
            max_v = temp
        return
    else:
        if plus:
            dfs(k + 1, temp + arr[k], plus - 1, minus, mul, div)
        if minus:
            dfs(k + 1, temp - arr[k], plus, minus - 1, mul, div)
        if mul:
            dfs(k + 1, temp * arr[k], plus, minus, mul - 1, div)
        if div:
            dfs(k + 1, int(temp / arr[k]), plus, minus, mul, div - 1)

N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, /

min_v = 9999999999
max_v = -9999999999

dfs(1, arr[0], op[0], op[1], op[2], op[3])

print(max_v)
print(min_v)
