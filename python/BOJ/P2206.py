import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
map = []
for _ in range(N):
    map.append(sys.stdin.readline().rstrip())
# print(map)

move = [[-1, 0], [0, -1], [1, 0], [0, 1]]

# 1. 실패
# visited = [[0 for m in range(M)] for n in range(N)]

# def bfs(x, y, b):
#     dq = deque()
#     dq.append((x, y, b))  # 현위치, 벽을 부순 횟수
#     visited[x][y] = 1
#     while dq:
#         # print(dq)
#         cur_x, cur_y, broken = dq.popleft()
#         for m_x, m_y in move:
#             new_x = cur_x + m_x
#             new_y = cur_y + m_y
#             if 0 <= new_x < N and 0 <= new_y < M:
#                 if map[new_x][new_y] == '1' and broken == 0:
#                     dq.append((new_x, new_y, 1))
#                     visited[new_x][new_y] = visited[cur_x][cur_y] + 1
#                 elif map[new_x][new_y] == '0' and visited[new_x][new_y] == 0:
#                     dq.append((new_x, new_y, broken))
#                     visited[new_x][new_y] = visited[cur_x][cur_y] + 1
#
#
# bfs(0, 0, 0)
# # print(visited)
# print(visited[N - 1][M - 1] if visited[N - 1][M - 1] > 0 else -1)

# 도착하기 위해서 벽을 부수거나 안 부수거나, 둘중에 골라야 하는 줄 알았다.
# 그게 아니라 벽을 안 부시고도 도착할 수 있고 부수고도 도착할 수 있으므로 두 상황 모두를 고려해야 한다.
# 그래서 사람들이 3차원 배열을 사용한 것이다.

# 2. 블로그 참조 -> Python(179688KB	5508ms) Pypy(275896KB	1512ms)
visited = [[[0] * 2 for m in range(M)] for n in range(N)]
# 3차원이 아니라 2(방문 안함), 1(벽 파괴), 0(방문)으로 표현한 사람도 있음
# 다 돌리는 게 아니라 최단경로를 탐색하는 거라서 2차원 배열에 저장 가능한 거 같다.


def bfs(x, y, b):
    dq = deque()
    dq.append((x, y, b))  # 현위치, 벽 파괴 여부
    visited[x][y][b] = 1
    while dq:
        # print(dq)
        cur_x, cur_y, broken = dq.popleft()

        if cur_x == N - 1 and cur_y == M - 1:
            return visited[cur_x][cur_y][broken]

        for m_x, m_y in move:
            new_x = cur_x + m_x
            new_y = cur_y + m_y
            if 0 <= new_x < N and 0 <= new_y < M:
                if map[new_x][new_y] == '1' and broken == 0:
                    dq.append((new_x, new_y, 1))
                    visited[new_x][new_y][1] = visited[cur_x][cur_y][0] + 1
                if map[new_x][new_y] == '0' and visited[new_x][new_y][broken] == 0:
                    dq.append((new_x, new_y, broken))
                    visited[new_x][new_y][broken] = visited[cur_x][cur_y][broken] + 1
    return -1


print(bfs(0, 0, 0))
# print(visited)
