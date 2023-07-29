t= int(input())

for q in range(1, t+1):
    n= int(input())
    
    now_list=[]
    for i in range(n):
        now_list.append([]) #[[], [], [], [], ~~]
    
    for x in range(n): #여기서부터 들여쓰기 하나 미뤄두고 왜 안 되는지 찾고 있었음
        for y in range(x+1):
            if x==0 or y==0 or y==x:
                now_list[x].append(1)
            else:
                now_list[x].append(now_list[x-1][y-1] + now_list[x-1][y])
    
    print(f'#{q}')
    for z in range(n):
        result = " ".join(map(str,now_list[z])) #map()으로 숫자가 포함된 리스트를 문자열로 변환
        
        print(result)
   
                
    
