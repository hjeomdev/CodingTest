import sys

K = int(sys.stdin.readline().rstrip())

w_max_idx = 0
h_max_idx = 1
w_max = 0
h_max = 0

ground = []
for i in range(6):
    direction, length = map(int, sys.stdin.readline().rstrip().split())
    ground.append(length)

    if direction == 1 or direction == 2:
        if w_max < length:
            w_max_idx = i
            w_max = ground[w_max_idx]
    elif direction == 3 or direction == 4:
        if h_max < length:
            h_max_idx = i
            h_max = ground[h_max_idx]

h_min = abs(ground[(w_max_idx - 1) % 6] - ground[(w_max_idx + 1) % 6])
w_min = abs(ground[(h_max_idx - 1) % 6] - ground[(h_max_idx + 1) % 6])

w_max = ground[w_max_idx]
h_max = ground[h_max_idx]

total = (w_max * h_max) - (w_min * h_min)
print(total * K)

# 검색함
# 육각형의 변이 순서대로 입력되고 가장 긴 너비와 높이가 서로 맡닿아 있기 때문에,
# 가장 긴 너비(또는 높이)의 양쪽 중에 가장 큰 높이(또는 너비)가 있다는 것을 알아차려야 풀 수 있는 문제다.

# abs(x)
# Doc: https://docs.python.org/3/library/functions.html?highlight=abs#abs
# 절댓값을 반환하는 함수