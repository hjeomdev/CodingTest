import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = []
R, B = [], []
for i in range(n):
    row = sys.stdin.readline().rstrip()
    for j in range(len(row)):
        if row[j] == 'R':
            R = [i, j]
        if row[j] == 'B':
            B = [i, j]
    matrix.append(row)


# print(n, m)
# for k in range(len(matrix)):
#     print(matrix[k])


def move(pos, d_x, d_y):
    px = pos[0]
    py = pos[1]
    c = 0
    while matrix[px + d_x][py + d_y] != '#' and matrix[px][py] != 'O':
        px += d_x
        py += d_y
        c += 1
    return px, py, c


def bfs(red, blue):
    dq = deque()
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    d = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    dq.append([red, blue, 1])
    visited[red[0]][red[1]][blue[0]][blue[1]] = 1

    while dq:
        r, b, cnt = dq.popleft()

        if cnt > 10:
            break

        for dx, dy in d:
            nrx, nry, rcnt = move(r, dx, dy)
            nbx, nby, bcnt = move(b, dx, dy)

            if matrix[nbx][nby] != 'O':
                if matrix[nrx][nry] == 'O':
                    print(cnt)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                if not visited[nrx][nry][nbx][nby]:
                    dq.append([[nrx, nry], [nbx, nby], cnt + 1])
                    visited[nrx][nry][nbx][nby] = True

        # for k in range(m):
        #     for t in range(n):
        #         print(visited[k][t])
        # print()

    print(-1)


bfs(R, B)
