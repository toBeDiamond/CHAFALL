def solution(s):
    answer = ''

    # 공백 처리
    words = s.split(' ')

    for i in range(len(words)):
        words[i] = words[i].capitalize()

    answer = " ".join(words)

    return answer

print(solution("3people unFollowed me"))


def solution(s):
    answer = ''

    # 공백 처리
    words = s.split(' ')

    for word in words:
        new_word = word.capitalize()
        answer += new_word + ' '

    # 마지막에 공백 있으니깐 날리기
    if answer and answer[-1] == ' ':
        answer = answer[:-1]

    return answer

print(solution("3people unFollowed me"))