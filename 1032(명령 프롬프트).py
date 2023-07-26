# n= int(input())
# text_list = []
# for x in range(n):
#     text_list.append(input())
    
# result=''
# # 첫번째 입력값을 고정시켜서 풀어보기
# for i in range(len(text_list[0])): #라인 하나씩 비교하기 위함
#     is_same = True
#     first_target = text_list[0][i] # 첫번째 입력값 하나씩 분해하기
#     for compare_text in text_list:
#         compare_target = compare_text[i] #비교할 것도 하나씩 분해하기
#         if first_target != compare_target: # 서로 비교하고 다르면 False출력
#             is_same = False
    
#     if is_same == True:          #다 같으면 원래의 값을 더함
#         result += first_target
    
#     else:                   #다르면 ?를 더해줌
#         result += '?'
# print(result)
    
#-------------------------------------------------------------------------------------

n= int(input())
first_text = list(input()) #하나만 미리 뻬기

for _ in range(n-1): #하나 미리 빼서 1 빼줌
    others_text = list(input()) # 나머지 텍스트 받기
    for i in range(len(first_text)):
        if first_text[i] != others_text[i]: #비교하기, 다르면 첫 text에 ? 넣기
            first_text[i] = '?'  

result =''.join(first_text) #리스트를 문자열로 변환
print(result)
