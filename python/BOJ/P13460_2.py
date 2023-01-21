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

# 두 번째 푸는 건데 여전히 못 풀어서 충격이다.
# 내가 놓친 부분은 빨간공과 파란공의 방문기록을 4차원으로 관리하지 않은 것이다.
# 처음 풀었을 때 남긴 코멘트에 따르면, 처음 풀 때도 똑같은 부분을 놓쳤다.
# 두 공을 모두 확인해야 하는 이유는, "빨간공의 위치가 같아도 파란공의 위치가 다르면 다른 경우"이기 때문이다.

# 4차원 배열에 대해 머릿속으로 이해가 안돼서 4차원 시공간에 대한 검색을 했다..
# 2차원이 카드고, 3차원은 카드 뭉치고, 4차원은 카드 뭉치가 여러개 있는 거라고 한다..
# 솔직히 지금도 이해가 완전히 되지 않는다.
# 외우더라도 다음번에 풀었으면 좋겠다.
# "dfs, bfs 문제에서 동시에 움직이는 것이 있다면, 4차원 배열로 방문기록을 할것!!!"
