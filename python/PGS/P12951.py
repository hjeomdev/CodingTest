def solution(s):
    answer = ''

    next_is_capitalize = False

    for i in range(len(s)):
        # print(answer, next_is_capitalize)
        if (i == 0 and not s[i].isnumeric()) or next_is_capitalize:
            answer += s[i].capitalize()
            next_is_capitalize = False
        else:
            answer += s[i].lower()

        if s[i] == ' ':
            next_is_capitalize = True

    return answer