# https://programmers.co.kr/learn/courses/30/lessons/68935
# 2022. 05. 26 / 30분
# 10 진법으로 바꿔주는 기능을 처음 알았다: int(숫자, 숫자의 진수)

def decimal_to_ternary(num):
    result = ''
    while num > 0:
        temp = num % 3
        result += str(temp)
        num = num // 3
    return result


def solution(n):
    answer = 0
    n = decimal_to_ternary(n)
    print(n)
    answer = int(n, 3)
    return answer
