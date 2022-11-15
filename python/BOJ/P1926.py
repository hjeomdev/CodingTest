import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
drawing = []
for _ in range(n):
    drawing.append(list(map(int, sys.stdin.readline().rstrip().split())))

# print(drawing)

count = 0
largest = 0

visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(start_x, start_y):
    dq = deque()
    dq.append((start_x, start_y))
    visited[start_x][start_y] = True
    cnt = 1
    while dq:
        cur_x, cur_y = dq.popleft()

        for x, y in zip(dx, dy):
            nex_x = cur_x + x
            nex_y = cur_y + y
            if 0 <= nex_x < n and 0 <= nex_y < m and not visited[nex_x][nex_y] and drawing[nex_x][nex_y] == 1:
                dq.append((nex_x, nex_y))
                visited[nex_x][nex_y] = True
                cnt += 1

    return cnt


for i in range(n):
    for j in range(m):
        if drawing[i][j] == 1 and not visited[i][j]:
            result = bfs(i, j)
            if result > 0:
                count += 1
                largest = max(largest, result)

print(count, largest, sep='\n')

# python(34192KB	544ms),  pypy3(122644KB	260ms)