import sys

xs = []
ys = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    xs.append(x)
    ys.append(y)

result_x = 0
result_y = 0

for i in range(3):
    if xs.count(xs[i]) == 1:
        result_x = xs[i]
    if ys.count(ys[i]) == 1:
        result_y = ys[i]

print(result_x, result_y)

# 뭔가 감은 오는데 문제를 관통하는 공통점은 찾지 못해서 고민하다가 검색함.
# 포인트가 되는 숫자의 개수였다.
# 포인트가 되는 숫자는 최소 2개에서 4개이다.
# 어떤 경우라도 각 수는 x좌표, y좌표에서 각각 최소 2번은 사용되어야 하기 때문에 1번만 사용된 경우 남은 꼭짓점이라고 판단할 수 있다.