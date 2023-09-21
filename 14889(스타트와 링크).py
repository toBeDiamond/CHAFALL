# def comb(n, r, k, s): # s는 시작 숫자
#     global min_v
#
#     if min_v == 0: return # 약간의 가지치기
#
#     # 아래를 수정
#     if r == k:
#         temp_p = 0
#         temp_q = 0
#
#         q = list(set(A) - set(p)) # 반대편 팀 만들기!!
#         for i in range(M):
#             for j in range(M):
#                 # 자기 자신은 계산 안해줘도 되므로, 주석 처리해도 됨(어차피 0이므로)
#                 if i == j:
#                     continue
#                 else:
#                     temp_p += arr[p[i]][p[j]]
#                     temp_q += arr[q[i]][q[j]]
#
#         if min_v > abs(temp_p - temp_q):
#             min_v = abs(temp_p - temp_q)
#     else:
#         for i in range(s, n - r + 1 + k):  # n - r + 1 :선택할 수 있는 마지막 원소
#             p[k] = A[i]
#             comb(n, r, k + 1, i + 1)
#
#
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# M = N // 2
# min_v = 99999999999
# A = list(range(N))
# p = [0] * M
# comb(N, M, 0, 0)
#
# print(min_v)

#-------------------------------------------------------------------------
# 백트래킹(양 팀으로 나눠서 생각)
def dfs(k, alst, blst):
    global min_v

    if min_v == 0: return  # 약간의 가지치기

    # 한팀이 이미 M명 초과인 경우(오히려 늘 수도 있다..)
    if len(alst) > M or len(blst) > M:
        return

    if k == N:
        if len(alst) == len(blst):  # 같은 인원수로 구성
            asm = bsm = 0
            for i in range(M):
                for j in range(M):
                    asm += arr[alst[i]][alst[j]]
                    bsm += arr[blst[i]][blst[j]]

            min_v = min(min_v, abs(asm-bsm))
        return

    dfs(k + 1, alst + [k], blst) # A팀 선택
    dfs(k + 1, alst, blst + [k]) # B팀 선택


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
M = N // 2
min_v = 99999999999
dfs(0, [], [])
print(min_v)