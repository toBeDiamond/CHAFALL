No_list = ['C', 'A', 'M', 'B', 'R', 'I', 'D' ,'G' ,'E']
text= input()

for chr in text:
    if chr in No_list:
        text = text.replace(chr, '') # replace는 비파괴라 리턴 받아야 함

print(text)

