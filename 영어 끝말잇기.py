def solution(n, words):
    N = len(words)

    people = 0; turn = 0
    for i in range(1, N):
        now = words[i]
        prev = words[i - 1]

        if prev[-1] != now[0] or now in words[:i]:
            people = i % n + 1
            turn = i // n + 1
            break  # 까먹지 말자!
    return [people, turn]

print(solution(3, 	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))