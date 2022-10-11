import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
ladders = dict()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    ladders[x] = y
snakes = dict()
for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    snakes[u] = v
# print(ladders, snakes)

visited = [0 for _ in range(101)]
start = 1
end = 100

dice = 6

def bfs(R, d):
    dq = deque()
    dq.append((R, d))
    visited[R] = 1
    while dq:
        current, depth = dq.popleft()

        if current in ladders:
            dq.append((ladders[current], depth))
        elif current in snakes:
            dq.append((snakes[current], depth))
        else:
            for i in range(1, dice + 1):
                new_cur = current + i
                if start <= new_cur <= end and (visited[new_cur] == 0 or visited[new_cur] > depth + 1):
                    dq.append((new_cur, depth + 1))
                    visited[new_cur] = depth + 1

bfs(start, 0)
# print(visited)
print(visited[100])

# 32484KB	84ms