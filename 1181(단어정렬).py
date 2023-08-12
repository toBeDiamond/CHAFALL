N = int(input())

char_set = set()
for n in range(N):
    char_set.add(input())
    char_list = list(char_set)
    
sort_char = []
for char in char_list:
    sort_char.append((len(char), char))

sorted_char = sorted(sort_char)
    

for char_len, char in sorted_char:
    print(char)

