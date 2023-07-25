n= int(input())
text_list = []
for x in range(n):
    text_list.append(input())
    
result=''
# 첫번째 입력값을 고정시켜서 풀어보기
for i in range(len(text_list[0])): #라인 하나씩 비교하기 위함
    is_same = True
    first_target = text_list[0][i] # 첫번째 입력값 하나씩 분해하기
    for compare_text in text_list:
        compare_target = compare_text[i] #비교할 것도 하나씩 분해하기
        if first_target != compare_target:
            is_same = False
    
    if is_same == True:
        result += first_target
    
    else:
        result += '?'
print(result)
    
