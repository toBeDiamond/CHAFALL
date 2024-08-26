# for문??
# 맨 앞은 제거하고 맨 뒤는 추가하는 방식으로 구현
# 앞 뒤로 넣고 빼는데 부담이 없는 자료구조는?
# deque
from collections import deque

def solution(want, number, discount):
    ans = 0
    # 원하는 것은 key로 수량은 value로 한 딕셔너리 생성
    info = dict(zip(want, number))
    check = {}
    N = len(discount)
    M = 10 # 회원 자격 10일

    # 초기 설정
    d = deque(discount[:M])
    for i in range(M):
        check[discount[i]] = check.setdefault(discount[i], 0) + 1
    if info == check:
        ans += 1

    for i in range(1, N - M + 1):
        # deque 처리
        left = d.popleft() # 맨 앞 삭제
        right = discount[i + M - 1]
        d.append(right) # 맨 뒤 추가
        # check 딕셔너리 처리
        check[left] -= 1
        if check[left] == 0:
            del check[left]  # count가 0인 항목은 제거
        check[right] = check.setdefault(right, 0) + 1

        # 비교
        if info == check:
            ans += 1

    return ans

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))


#--- 카운터를 이용한 다른 방식
from collections import Counter
def solution(want, number, discount):
    ans = 0
    # 원하는 것은 key로 수량은 value로 한 딕셔너리 생성
    info = dict(zip(want, number))
    N = len(discount)

    for i in range(N - 10 + 1):
        if info == Counter(discount[i: i + 10]):
            ans += 1

    return ans

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))