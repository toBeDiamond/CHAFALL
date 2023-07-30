t = int(input())
for x in range(t):
    n, m = map(int,input().split())

    n_list = list(range(1, n+1)) # [1, 2, 3, 4, 5 .. ]이런식으로 받아서 하나씩 곱하기 쉽게
    m_list = list(range(1, m+1))
    
    #mCn 
    top = 1                 #분자part
    for ml in m_list[m-n:]: 
        top*=ml
    
    bottom = 1              #분모part
    for nl in n_list:
        bottom*=nl
    
    result = top / bottom
    print(int(result))
   

#-----------------------------------
# 구현해보고 싶은거=> 7C5는 7C2로 해서 풀기

