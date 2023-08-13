# N = int(input())
# score = []
# for _ in range(N):
#     score.append(int(input()))
#
# max_score = score[-1]
#
# i = N-2
# j = 1
# gap = 0
# while i >= 0:
#     gap += abs(max_score - j - score[i])
#
#     i -= 1
#     j += 1
#
# print(gap)

#------------------------------------------------------
# 위의 방식 틀린 이유: 굳이 한 칸씩 내려갈 필요 없구나...

N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

gap = 0
for i in range(N-2, -1, -1):
    if score[i] >= score[i+1]:
        gap -= score[i + 1] - 1 - score[i]
        score[i] = score[i+1] -1

print(gap)