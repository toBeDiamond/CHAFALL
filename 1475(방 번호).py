# 6 한개를 건들면 9도 한개 같이 날아가는 방식으로 구현
S = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9]
N = list(map(int,input()))

# 초기 설정
s = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9]
counts = 1

for n in N:
        # 없으면 extend 함수를 써서 S 넣어줌
    if n not in s:
        s.extend(S)
        counts += 1

    if n in s and n != 6 and n!= 9:
        s.remove(n)
        # 6 한개를 건들면 9도 한개 같이 날아감(반대도 동일)
    elif n in s and (n == 6 or n== 9):
        s.remove(6)
        s.remove(9)

print(counts)