# https://programmers.co.kr/learn/courses/30/lessons/68644
# 2022. 05. 26 / 15분

def solution(numbers):
    answer = []
    result = set() # 중복 제거
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j: # 서로 다른 인덱스에 있는 두 수
                result.add(numbers[i] + numbers[j])
    answer = list(result)
    return sorted(answer) # 정렬