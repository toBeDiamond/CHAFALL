# 갈색 수 = 2 * (노란색의 가로) + 2 * (노란색의 세로) + 4

def solution(brown, yellow):
    answer = []

    y_width = 0  # 노란색 가로
    y_length = 0  # 노란색 세로

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_width = yellow // i
            y_length = i
            if (2 * y_width + 2 * y_length + 4) == brown:
                answer.append(y_width + 2)
                answer.append(y_length + 2)

                answer.sort(reverse=True)
                return answer

print(solution(8, 1))