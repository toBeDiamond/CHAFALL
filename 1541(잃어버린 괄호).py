# num_list = list(input().split('-'))
# # 처음 것만 냅두고 나머진 다 빼주면 될 듯함
# for i in range(1, len(num_list)):
#
#     num_list[i] = '-('+num_list[i] + ')'
#
# print(eval(''.join(num_list)))

#---------------------------------------------------
num_list = input().split('-')
total = 0
# 모두 양수일 수도 있으므로 처음것도 이렇게
for num in num_list[0].split('+'):
    # 첫 숫자가 음수라면? 처음에 빈 것 나와서 에러뜸
    if num == '':
        num = 0
    total += int(num)

for num in num_list[1:]:
    nu = num.split('+')
    for n in nu:
        total -= int(n)
print(total)




