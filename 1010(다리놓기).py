t = int(input())
for x in range(t):
    n, m = map(int,input().split())

    n_list = list(range(1, n+1))
    #n_list = n_list[::-1]
    m_list = list(range(1, m+1))
    #m_list = m_list[::-1]

    
    
    top = 1
    for ml in m_list[m-n:]:
        top*=ml
    
    bottom = 1
    for nl in n_list:
        bottom*=nl
    
    result = top / bottom
    print(int(result))
   

#-----------------------------------
# 구현해보고 싶은거=> 7C5는 7C2로 해서 풀기

