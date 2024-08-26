# stack 이용!

def solution(s):
    answer = -1
    N = len(s)
    stack = []

    for i in range(N):
        if not stack:
            stack.append(s[i])
        else:
            # 지금 넣을 놈과 스택 마지막 놈 비교
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])

    # 다 돌았을 때 비어있으면
    if not stack:
        return 1
    else:
        return 0

print(solution("baabaa"))
