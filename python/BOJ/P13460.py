import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())  # 세로, 가로
board = [['' for m in range(M)] for n in range(N)]
# visited = [[0 for m in range(M)] for n in range(N)]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

red = []
blue = []
goal = []
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    for j in range(len(temp)):
        if temp[j] == 'R':
            red = [i, j]
            board[i][j] = "."
        elif temp[j] == 'B':
            blue = [i, j]
            board[i][j] = "."
        else:
            board[i][j] = temp[j]
            # if temp[j] == 'O':
            #     goal = [i, j]
# print(board, red, blue)

# . 빈칸 # 장애물 및 가장자리 벽 0 구멍 R 빨간구슬 B 파란구슬

# 1. 실패
# def bfs(R, B):
#     dq = deque()
#     dq.append([R, B])
#     visited[R[0]][R[1]] = 1
#     while dq:
#
#         r, b = dq.popleft()
#         print("rb", r, b)
#         if b[0] == goal[0] and b[1] == goal[1]:
#             continue
#         if r[0] == goal[0] and r[1] == goal[1]:
#             for k in range(len(visited)):
#                 print(visited[k])
#             print()
#             print(visited[r[0]][r[1]] - 1)  # 1로 시작해서 빼줌
#             break
#
#         if visited[r[0]][r[1]] > 10:
#             print(-1)
#             break
#
#         def move(direct, u, v):
#             u_x, u_y = [u[0], u[1]]  # u's result
#             v_x, v_y = [v[0], v[1]]  # v's result
#             trigger = 0
#             if direct == 'up':
#                 while trigger < 2:
#                     if 0 <= u_x - 1 < N and (u_x - 1 != v_x and u_y != v_y):
#                         u_x -= 1
#                         if board[u_x][u_y] == '#':
#                             u_x += 1
#                             trigger += 1
#                         elif goal[0] == u_x and goal[1] == u_y:
#                             trigger += 1
#                     if 0 <= v_x - 1 < N and (u_x != v_x - 1 and u_y != v_y):
#                         v_x -= 1
#                         if board[v_x][v_y] == '#':
#                             v_x += 1
#                             trigger += 1
#                         elif goal[0] == v_x and goal[1] == v_y:
#                             trigger += 1
#             elif direct == 'left':
#                 while trigger < 2:
#                     if 0 <= u_y - 1 < M and (u_x != v_x and u_y - 1 != v_y):
#                         u_y -= 1
#                         if board[u_x][u_y] == '#':
#                             u_y += 1
#                             trigger += 1
#                         elif goal[0] == u_x and goal[1] == u_y:
#                             trigger += 1
#                     if 0 <= v_y - 1 < M and (u_x != v_x and u_y != v_y - 1):
#                         v_y -= 1
#                         if board[v_x][v_y] == '#':
#                             v_y += 1
#                             trigger += 1
#                         elif goal[0] == v_x and goal[1] == v_y:
#                             trigger += 1
#             elif direct == 'down':
#                 trigger = 0
#                 while trigger < 2 or (u_x + 1 >= N and v_x + 1 >= N):
#                     if 0 <= u_x + 1 < N and (u_x + 1 != v_x and u_y != v_y):
#                         u_x += 1
#                         if board[u_x][u_y] == '#':
#                             u_x -= 1
#                             trigger += 1
#                         elif goal[0] == u_x and goal[1] == u_y:
#                             trigger += 1
#                     if 0 <= v_x + 1 < N and (u_x != v_x + 1 and u_y != v_y):
#                         v_x += 1
#                         if board[v_x][v_y] == '#':
#                             v_x -= 1
#                             trigger += 1
#                         elif goal[0] == v_x and goal[1] == v_y:
#                             trigger += 1
#             elif direct == 'right':
#                 while trigger < 2:
#                     if 0 <= u_y + 1 < M and (u_x != v_x and u_y + 1 != v_y):
#                         u_y += 1
#                         if board[u_x][u_y] == '#':
#                             u_y -= 1
#                             trigger += 1
#                         elif goal[0] == u_x and goal[1] == u_y:
#                             trigger += 1
#                     if 0 <= v_y + 1 < M and (u_x != v_x and u_y != v_y + 1):
#                         v_y += 1
#                         if board[v_x][v_y] == '#':
#                             v_y -= 1
#                             trigger += 1
#                         elif goal[0] == v_x and goal[1] == v_y:
#                             trigger += 1
#                 print(u_x, u_y, v_x, v_y)
#             u_r = [u_x, u_y]
#             v_r = [v_x, v_y]
#             print("move result", u_r, v_r)
#             return u_r, v_r
#
#         for d in ['right', 'up', 'left', 'down']:
#             print("d", d)
#             new_r, new_b = move(d, r, b)
#
#             if new_r[0] == new_b[0] and new_r[1] == new_b[1]:
#                 continue
#
#             if visited[new_r[0]][new_r[1]] == 0:
#                 dq.append([new_r, new_b])
#                 print("before", visited[r[0]][r[1]], r)
#                 visited[new_r[0]][new_r[1]] = visited[r[0]][r[1]] + 1
#                 print("wrong", visited[new_r[0]][new_r[1]], visited[r[0]][r[1]])
#
#
# bfs(red, blue)
# for k in range(len(visited)):
#     print(visited[k])

# 헉... 한칸씩 움직이는게 아니라 중력을 이용해서 움직이는 거임..

# move()에서 장애물, 구멍, "다른 공의 위치"를 계속 확인하면서 반복문을 돌려야함

# 코드가 너무 길어져서 답을 봤다. https://wlstyql.tistory.com/72
# 내가 내 발등을 찍어내고 있었다.. 불필요한 코드가 너무 많다.
# RB가 나란히 같이 움직이는 경우에는 가장 동선이 긴 공을 -1 하는 방법을 참고해서 다시 작성하겠다.


# 2.
d = [[-1, 0], [0, -1], [0, 1], [1, 0]]


def move(x, y, d_x, d_y):
    cnt = 0
    while board[x + d_x][y + d_y] != '#' and board[x][y] != 'O':
        x += d_x
        y += d_y
        cnt += 1
    return x, y, cnt


def bfs(R):
    dq = deque()
    dq.append((R[0][0], R[0][1], R[1][0], R[1][1], 1))
    visited[R[0][0]][R[0][1]][R[1][0]][R[1][1]] = True
    while dq:
        rx, ry, bx, by, depth = dq.popleft()

        if depth > 10:
            break

        for m_x, m_y in d:
            nrx, nry, rcnt = move(rx, ry, m_x, m_y)
            nbx, nby, bcnt = move(bx, by, m_x, m_y)

            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    print(depth)
                    return
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= m_x
                        nry -= m_y
                    else:
                        nbx -= m_x
                        nby -= m_y
                if not visited[nrx][nry][nbx][nby]:
                    dq.append((nrx, nry, nbx, nby, depth + 1))
                    visited[nrx][nry][nbx][nby] = True
    print(-1)


bfs([red, blue])

# 32556KB	88ms
# 빨간 구슬과 파란 구슬을 같이 저장해야 한다.
# 빨간 구슬이 같은 위치에 있더라도 파란 구슬 위치가 다르면 다른 상황이기 때문이다.
