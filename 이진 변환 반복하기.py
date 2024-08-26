def solution(s):

    transform_cnt = 0
    zero_cnt = 0

    while s != "1":
        # 0 갯수 세고 변환
        zero_cnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        # [2:]를 다는 이유는 '0b'를 지우기 위함.
        transform_cnt += 1

    return [transform_cnt, zero_cnt]

print(solution("110010101001"))