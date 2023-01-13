def solution(babbling):
    answer = 0

    available = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        cur = babbling[i]
        for a in available:
            if a in cur:
                cur = cur.replace(a, ' ')
        if len(cur.strip()) == 0:
            answer += 1

    return answer