# https://programmers.co.kr/learn/courses/30/lessons/70128
# 2022. 05. 26 / 1분

def solution(a, b):
    answer = 0
    for a, b in zip(a, b):
        answer += a * b
    return answer