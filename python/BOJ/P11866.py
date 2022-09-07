import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
# print(N, K)

dq = deque([i for i in range(1, N + 1)])
# print(dq)

# answer = "<"
# while len(dq) > 0:
#     # print(dq)
#     dq.rotate((K - 1) * -1)
#     answer += str(dq.popleft())
#     if len(dq) > 0:
#         answer += ", "
#
# answer += ">"
# print(answer)

# 프린트 방식 변경
answer = []
while len(dq) > 0:
    # print(dq)
    dq.rotate((K - 1) * -1)
    answer.append(str(dq.popleft()))

print('<', ', '.join(answer), '>', sep='')

# 32416KB	88ms