No_list = ['C', 'A', 'M', 'B', 'R', 'I', 'D' ,'G' ,'E']
text= input()

for chr in text:
    if chr in No_list: # 해당 문자가 no리스트에 있으면 바꿔줌
        text = text.replace(chr, '') # replace는 비파괴라 리턴 받아야 함

print(text)