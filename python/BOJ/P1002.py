import sys
import math

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    # print("dis", distance)
    answer = 0
    if distance == 0:
        if r1 == r2:
            sys.stdout.write(str(-1) + '\n') # 두 원이 겹쳐져 하나처럼 보이는 경우
        else:
            sys.stdout.write(str(0) + '\n')
    else:
        if distance < r1 + r2 and (distance > abs(r1 - r2)):
            sys.stdout.write(str(2) + '\n')
        elif distance == r1 + r2 or abs(r2 - r1) == distance:
            sys.stdout.write(str(1) + '\n')
        else:
            sys.stdout.write(str(0) + '\n')

# 중심점이 다른데 원 안에 원이 있는 경우를 생각 못함
# 출저: https://itstory1592.tistory.com/33