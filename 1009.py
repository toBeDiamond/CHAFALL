# t = int(input())
# for x in range(t):
#     a, b = map(int,input().split())
#     result = (a ** b) % 10
#     print(result)


#-------------------------------------------

num_dict={
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
    a %= 10
    
    if a==1 or a==5 or a==6:
        result = a
    elif a==2 or a==3 or a==7 or a==8:
        result = num_dict[a][b%4-1]
    elif a==4 or a==9:
        result = num_dict[a][b%2-1]
    
    print(result)
#-------------------------------------------------왜틀림?