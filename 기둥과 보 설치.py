#[x, y, a, b]
# a -> 0 : 기둥, 1 : 보
# b -> 0 : 삭제, 1 : 설치
# 보는 오르쪽, 기둥은 위쪽으로 설치/삭제 됨.

# 설치 가능 여부 체크
def check(ans):
    for x, y, a in ans:
        # 기둥일 때
        if a == 0:
            # 기둥이 바닥 위 or 다른 기둥 위 or 보의 한쪽 끝
            if y == 0 or [x, y - 1, 0] in ans or [x - 1, y, 1] in ans\
                    or [x, y, 1] in ans:
                continue # 딴 놈도 체크해야 되므로
            # 여기 밑으로 내려왔다면? 조건 불충분으로
            return False

        # 보일 때
        else:
            # 보의 한쪽 끝이 기둥 위 or 양쪽 끝이 동시에 다른 보에 연결
            if [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans or\
                    ([x - 1, y , 1] in ans and [x + 1, y, 1] in ans):
                continue
            return False
    # 모든 것이 조건을 통과한다면?
    return True

def solution(n, build_frame):
    answer = []

    for bf in build_frame:
        x, y, a, b = bf

        # 설치 시
        if b == 1:
            answer.append([x, y, a])  # 일단 넣어
            # 조건 불충분하면 다시 빼
            if not check(answer):
                answer.remove([x, y, a])
        # 삭제 시
        else:
            answer.remove([x, y, a])  # 일단 빼
            # 조건 불충분하면 다시 넣어
            if not check(answer):
                answer.append([x, y, a])

    answer.sort()

    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))

