# 키: 왼쪽 괄호
# 값: 키에 해당하는 알맞은 오른쪽 괄호
info = {}
# 리턴 숫자로
def check(new_s):
    stack = []

    for n_s in new_s:
        # 왼쪽 괄호면 무조건 넣음
        if n_s in info.keys():
            stack.append(n_s)
        # 오른쪽 괄호이면
        elif n_s in info.values():
            # 짝지가 없으면
            if not stack:
                return 0
            # 올바른 짝지가 바로 위에 있다면
            elif n_s == info[stack[-1]]:
                stack.pop()
            # 올바른 짝지가 아니라면
            else:
                return 0
    # 다 돌았는데 왼쪽 괄호가 남아있다면
    if stack:
        return 0

    # 모든 관문을 통과했으면
    return 1

def solution(s):

    info['('] = ')'; info['{'] = '}'; info['['] = ']'
    N = len(s)

    cnt = 0
    for i in range(N):
        new_s = s[i:] + s[:i]
        cnt += check(new_s)

    return cnt

print(solution("[](){}"))