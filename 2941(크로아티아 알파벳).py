Cro_alphabet_list= ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
text = input()

# Cro_alphabet_list안에 값이 있으면 그 값을 @로 변환
for Cro_alphabet in Cro_alphabet_list:
    text = text.replace(Cro_alphabet, '@') 
# print(text)
print(len(text))


# 딕셔너리 키 안에 있는지 알아내는 방법 찾기
# 주의사항: dz= 와 z=의 리스트 순서 고려하기
