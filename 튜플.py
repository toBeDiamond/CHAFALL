def solution(s):

    answer = []
    transform = [] # 변화된 형태를 담을 리스트

    # 변환 작업
    info = s.split("},")
    for i in info:
        transform.append(i.replace("{", "").replace("}", "").split(","))

    # 크기 순으로 sort
    transform.sort(key=len)

    for tr in transform:
        for i in tr:
            if not int(i) in answer:
                answer.append(int(i))

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
