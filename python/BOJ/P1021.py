import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
selected = list(map(int, input().rstrip().split()))
# print(N, M, selected)

dq = deque([i for i in range(1, N + 1)])
answer = 0
for i in selected:
    # print(dq)
    cur = dq[0]
    if i == cur:
        dq.popleft()
    else:
        idx = dq.index(i)
        mid = len(dq) // 2
        move = 0
        if idx <= mid:  # 시계 반대방향 회전
            move = idx
            dq.rotate(-idx)
        else:  # 시계방향 회전
            move = len(dq) - idx
            dq.rotate(move)
        answer += move
        dq.popleft()
print(answer)

# 32452KB	88ms