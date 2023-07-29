# t =  int(input())

# num_list = list(map(int, input().split()))
# num_list.sort()

# result = num_list[0] * num_list[-1]
# print(result)

#-------------------------------------------------

t =  int(input())

num_list = list(map(int, input().split()))
new_num_list = sorted(num_list)

result = new_num_list[0] * new_num_list[-1]
print(result)