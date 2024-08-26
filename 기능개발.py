from collections import deque

def solution(progresses, speeds):
    answer = []

    N = len(progresses)

    # 걸리는 일수를 담을 리스트
    times = deque()

    # 걸리는 일수들 구해주기
    for i in range(N):
        cnt = 1
        while True:
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                break
            cnt += 1
        times.append(cnt)

    print(times)

    # 배포에 걸리는 시간은 모두에게 해당이 되므로 따로 배포 카운트를 해줄 필요는 없음

    now = times.popleft()
    build_cnt = 1
    while times:
        # 지금놈 보다 다음놈이 더 빨리 또는 같이 완료가 되었다면 같이 빌드
        if now >= times[0]:
            times.popleft()
            build_cnt += 1
        else:
            now = times.popleft()
            answer.append(build_cnt)
            build_cnt = 1

    answer.append(build_cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
#-----


def solution(progresses, speeds):
    answer = []

    N = len(progresses)

    # 걸리는 일수를 담을 리스트
    times = deque()

    # 걸리는 일수들 구해주기
    for i in range(N):
        cnt = 1
        while True:
            progresses[i] += speeds[i]
            if progresses[i] >= 100:
                break
            cnt += 1
        times.append(cnt)

    now = times.popleft()
    build_cnt = 1
    while times:
        next = times.popleft()
        # 지금놈 보다 다음놈이 더 빨리 또는 같이 완료가 되었다면 같이 빌드
        if now >= next:
            build_cnt += 1
        else:
            now = next
            answer.append(build_cnt)
            build_cnt = 1

    answer.append(build_cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
#---
