from itertools import product


def solution(word):
    answer = 0

    chars = ['A', 'E', 'I', 'O', 'U']
    d = []
    for i in range(1, 6):
        d.extend(''.join(i) for i in product(chars, repeat=i))

    d.sort()

    # 문자열 -> 아스키
    # for i in d[0:800]:
    #     print(i, [ord(c) for c in i])

    for i in range(len(d)):
        if d[i] == word:
            answer = i + 1
            break

    return answer

# 5글자로 길이가 5인 단어를 만들면 최대 3125개를 만들 수 있다.
# 생성 및 정렬하는 시간 복잡도가 작기 때문에 미리 만들어서 사용 가능하다.
# 아스키 코드를 기준으로 정렬하되 지수정렬 알고리즘(각 자리의 수를 비교해서 정렬)을 사용해서 정렬하는 듯하다!

solution('AA')

# ord(c)
# https://docs.python.org/ko/3/library/functions.html?highlight=ord#ord
