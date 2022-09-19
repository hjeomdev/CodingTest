import sys

input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())


# print(a, b, c)

# 1.
# answer = (a ** b) % c
# print(answer)

# 설마 위 코드겠어 하면서 아래 코드 작성했는데

# 2.
# answer = a
# for _ in range(b):
#     answer *= a
#     if answer > c:
#         answer %= c
# print(answer)

# 시간초과로 실패...

# 3.
# 모듈러 연산 사용하기
# (a + b) mod n = ((a mod n) + (b mod n)) mod n
# (a - b) mod n = ((a mod n) - (b mod n)) mod n
# (a * b) mod n = ((a mod n) * (b mod n)) mod n

# answer = a
# for _ in range(b):
#     answer = ((answer % c) * (a % c)) % c
#
# print(answer)

# 이것도 시간초과로 실패...

# 4.
# 지수법칙과 나머지 분배법칙을 응용하면 된다고 한다

# 지수법칙을 이용해서 제곱하는 과정을 최대한 줄인다.
# 예를 들어,
# 10^11이면 (10^5) * (10^5) * 10 으로 5번만 제곱해서 그걸 가지고 결과를 얻을 수 있다는 것이다.
# 10^10이면 (10^5) * (10^5)이다.
# 그래서 b가 홀수인지 짝수인지 확인해서 결과를 반환한다.

# 여기에 나머지 분배 법칙을 적용해서 수가 커지는 것을 막는다.

def squared(a, n):
    if n == 1:
        return a % c
    else:
        temp = squared(a, n // 2)
        if n % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c

print(squared(a, b))

# 30840KB	72ms

# 5.
# pow(base, exp[, mod])
# https://docs.python.org/ko/3/library/functions.html?highlight=pow#pow
# base의 exp 거듭제곱을 돌려주고 mod가 있다면 나머지를 반환해준다.

# print(pow(a, b, c))