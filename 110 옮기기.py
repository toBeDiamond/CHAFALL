def solution(s):
    answer = []
    return answer

print(solution(["1110","100111100","0111111010"]))


def solution(s):
    # 110을 새로 넣어서 110이 나타나는 경우가 있을까요? 없습니다.
    # 0 110 0
    # 0 110 1
    # 1 110 0
    # 1 110 1
    # 따라서 문자열에서 110이 나타날 때마다 제거하는 식으로,
    # 문자열에서 나타나는 모든 110의 경우를 알아낼 수 있습니다.
    # 110을 모두 제거한 문자열과, 110의 개수를 우선 얻어보자.
    # 스택으로 해결하면 됩니다.
    answer = []
    for arr in s:
        stack, num110, i = [], 0, 0
        while i < len(arr):
            if arr[i] == '0':
                if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1':
                    stack.pop()
                    stack.pop()
                    num110 += 1
                    i += 1
                else:
                    stack.append(arr[i])
                    i += 1
            else:
                stack.append(arr[i])
                i += 1

        # 뒤에서부터 읽어가면서, 처음 나타나는 0 뒤에 110들을 다 붙여줍니다.
        # 우선 stack을 뒤집고 0을 찾으면 뒤에서부터 몇 번째(0-based)에 0이 처음으로 나오는지 셉니다.
        stack = ''.join(stack[::-1])
        idx = stack.find('0')

        if idx != -1:
            # 0이 있으면 뒤에 붙입니다.
            res = stack[:idx] + '011' * num110 + stack[idx:]
        else:
            # 0이 없으면 그냥 맨 앞에 붙입니다.
            res = stack + '011' * num110
        answer.append(''.join(res[::-1]))

    return answer

# 110 다 추출하고 111앞에 넣기
def solution(s):
    answer = []

    for string in s:
        stack = []
        count_110 = 0
        for str in string:
            # 110이 나온 경우
            if(len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and str == '0'):
                count_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(str)

        # 110을 모두 제거했으므로 남은 문자열에서 연속된 1이 존재하는 곳은 한 곳밖에 없다.
        count_1 = 0
        for s in stack[::-1]:
            if s == '0':
                break
            else:
                count_1 += 1
        answer.append(''.join(stack[:len(stack) - count_1]) + '110' * count_110 + '1' * count_1)
    return answer