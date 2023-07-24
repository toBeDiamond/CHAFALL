t = int(input())
for x in range(t):
    n, m = map(int,input().split())

    n_list = list(range(1, n+1))
    n_list = n_list[::-1]
    m_list = list(range(1, m+1))
    m_list = m_list[::-1]

    top = 1
    for nl in n_list[: n-m]:
        top*=nl
    bottom = 1
    for ml in m_list:
        bottom*=ml

    result = top / bottom
    print(result)
   

#-----------------------------------
# 구현해보고 싶은거=> 7C5는 7C2로 해서 풀기
print(29 * 28 * 27 * 26 * 25 * 24 * 23 * 22 * 21 * 20 * 19 * 18 * 17 / 13 / 12 / 11 /10 /9 /8 /7 /6 /5 /4 /3 /2)

#  [n-m:]