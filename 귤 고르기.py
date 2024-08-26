import heapq

def solution(k, tangerine):

    num = len(tangerine) # 귤 전체 수로 초기화

    # 종류별 갯수를 구할 딕셔너리
    info = {}
    # 각 종류별 귤 갯수에 대한 최소힙
    cnt_heap = []

    # 종류별 갯수 정보 구하기 (딕셔너리)
    for tang in tangerine:
        info[tang] = info.setdefault(tang, 0) + 1

    # 종류별 갯수 최소힙에 집어넣기
    for cnt in info.values():
        heapq.heappush(cnt_heap, cnt)

    while num >= k:
        now_cnt = heapq.heappop(cnt_heap)
        num -= now_cnt

    return len(cnt_heap) + 1

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
#-----------------

def solution(k, tangerine):
    answer = 0

    num = len(tangerine) # 귤 전체 수로 초기화

    # 종류별 갯수를 구할 딕셔너리
    info = {}

    # 종류별 갯수 정보 구하기 (딕셔너리)
    for tang in tangerine:
        if tang in info:
            info[tang] += 1
        else:
            info[tang] = 1

    # 딕셔너리도 sort가 되는구나,
    new_info = dict(sorted(info.items(), key=lambda x: x[1], reverse=True))
    for new_i in new_info.values():
        if k <= 0:
            return answer
        k -= new_i
        answer += 1

    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))