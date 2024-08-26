def solution(arr):

    num = max(arr)
    while True:
        cnt = 0
        for i in arr:
            if num % i == 0:
                cnt += 1
            else:
                num += 1
                break
        if cnt == len(arr):
            break
    return num

print(solution([2,6,8,14]))