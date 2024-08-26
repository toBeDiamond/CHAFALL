# 뒤에서부터 순회하면서 문제를 해결할려고 했는데
# 반례가 너무 많아서 포기

def solution(n):

    b_n = bin(n)[2:]  # 2진수로 변환 ('0b'뺀)
    n_cnt = b_n.count('1')

    for i in range(n + 1, 2 * n + 1):
        next_cnt = bin(i)[2:].count('1')

        if n_cnt == next_cnt:
            return i


print(solution(78))
