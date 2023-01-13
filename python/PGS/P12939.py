def solution(s):
    answer = ''

    s_int = list(map(int, s.split()))
    answer += str(min(s_int))
    answer += ' '
    answer += str(max(s_int))

    return answer