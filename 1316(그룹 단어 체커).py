T= int(input())
group_number = T
for tc in range(T):
    text = input()
    
    for i in range(len(text)-1): #단어 개수보다 한칸 앞까지
        if text[i] != text[i+1]: #연달은 두 문자가 달랐을 때
            if text[i] in text[i+1 :]: # i 값이 뒤에 또 나오나요?
                group_number-=1
                break
    
    
print(group_number)

        


        

