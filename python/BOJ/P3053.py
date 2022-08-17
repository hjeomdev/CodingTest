import sys
import math

R = int(sys.stdin.readline().rstrip())

sys.stdout.write(str(math.pi * R ** 2) + '\n')
sys.stdout.write(str(R * R * 2) + '\n')

# 당최 무슨 말인지 몰라서 검색했는데
# 유클리드 기하학에서 원은 우리가 아는 그 원이고
# 택시 기하학에서 원은 사각형이라고 한다..
# 출처: https://leedakyeong.tistory.com/entry/백준-3053번-택시-기하학-in-파이썬-쉽게-풀어보기 [슈퍼짱짱:티스토리]
# 택시 기하학이란거 이 문제에서 지어낸 건 줄 알았는데.. 생각도 못했다.

