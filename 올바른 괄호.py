# 스택으로 구현
# 조건 1 : 닫는 괄호가 여는 괄호보다 먼저 오면 안됨.
# 조건 2 : 쌍이 맞으면 소멸.
# 조건 3 : 다 끝났는데 여는 괄호가 남아있으면 안됨.

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            # 비었는데 닫는 괄호 오면 No
            if not stack:
                return False
            # 스택 안에 여는 괄호가 있다면
            # 쌍을 이뤄 소멸하는 느낌
            else:
                stack.pop()

    # 다 돌았는데 stack에 여는 괄호 남아있으면 No
    if stack:
        return False

    return True

print(solution("()()"))