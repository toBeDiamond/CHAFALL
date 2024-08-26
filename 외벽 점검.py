# n: 외벽의 길이 , weak:취약 지점의 위치, dist: 이동가능 거리
from itertools import permutations

def solution(n, weak, dist):
    answer = 987654321
    weak_len = len(weak)

    # 원형을 선형으로 (방향 고려 x 하기 위해)
    # 어떻게??? 10에서 13으로 넘어갈 때를 생각해봐! (n = 12일때)
    weak_linear = weak + [w + n for w in weak]

    # 출발 위치
    for i, start in enumerate(weak):
        for friends in permutations(dist): # 순열
            cnt = 1
            pos = start
            # 친구 조합 배치
            for friend in friends:
                pos += friend
                # 끝 포인트까지 도달 x했다면?
                # (한 바퀴 돈)
                if pos < weak_linear[i + weak_len - 1]:
                    cnt += 1  # 친구 더 투입
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로

                    # 1. 현재 취약 지점 이후의 취약 지점들 구하기
                    # 2. 그 중 현재 위치보다 큰 취약 지점 필터링
                    # 3. 그 중 첫번째 놈을 뽑아냄!
                    pos = [w for w in weak_linear[i + 1 :i + weak_len] if w >pos][0]
                # 끝 포인트까지 도달
                else:
                    answer = min(answer, cnt)

    if answer == 987654321:
        answer = -1

    return answer

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))

# 파이썬
# def solution(n, weak, dist):
#
#     W, F = len(weak), len(dist)
#     repair_lst = [()]  # 현재까지 고칠 수 있는 취약점들 저장 (1,2,3)
#     count = 0  # 투입친구 수
#     dist.sort(reverse=True) # 움직일 수 있는 거리가 큰 친구 순서대로
#
#     # 고칠 수 있는 것들 리스트 작성
#     for can_move in dist:
#         repairs = []  # 친구 별 고칠 수 있는 취약점들 저장
#         count += 1
#
#         # 수리 가능한 지점 찾기
#         for i, wp in enumerate(weak):
#             start = wp  # 각 위크포인트부터 시작
#             ends = weak[i:] + [n+w for w in weak[:i]]  # 시작점 기준 끝 포인트 값 저장
#             can = [end % n for end in ends if end -
#                    start <= can_move]  # 가능한 지점 저장
#             repairs.append(set(can))
#
#         # 수리 가능한 경우 탐색
#         cand = set()
#         for r in repairs:  # 새친구의 수리가능 지점
#             for x in repair_lst:  # 기존 수리가능 지점
#                 new = r | set(x)  # 새로운 수리가능 지점
#                 if len(new) == W:  # 모두 수리가능 한 경우 친구 수 리턴
#                     return count
#                 cand.add(tuple(new))
#         repair_lst = cand
#
#     return -1

