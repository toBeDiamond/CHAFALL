t = int(input())
for x in range(t):
    a, b = map(int,input().split())
    result = (a ** b) % 10
    print(result)


#-------------------------------------------

num_dict={           # 일의 자릿수 규칙 딕셔너리에 대입 
    1 : [1],
    2 : [2, 4, 8, 6],
    3 : [3, 9, 7, 1],
    4 : [4, 6],
    5 : [5],
    6 : [6],
    7 : [7, 9, 3, 1],
    8 : [8, 4, 2, 6],
    9 : [9, 1]
}

t = int(input())
for x in range(t):
    a, b = map(int,input().split())
    a %= 10   # 일의 자리만 알면 되므로 10의 나머지를 구함
    
    if a==1 or a==5 or a==6:  # 1, 5, 6일때는 값이 하나뿐이므로 그냥 바로 넣기 
        result = a
    elif a==2 or a==3 or a==7 or a==8: # a가 다음과 같을 때는 로테이션이 4이므로 b값을 4로 나눠주고
        result = num_dict[a][b%4-1]    # 인덱스를 맞춰주기 위해 1을 뺌
    elif a==4 or a==9:
        result = num_dict[a][b%2-1]    #위와 같음
    
    print(result)
#-------------------------------------------------왜틀림?