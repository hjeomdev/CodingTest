import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().rstrip().split())
box = []
affect = [[-1, 0, 0], [1, 0, 0], [0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0]]  # 위 아래 왼쪽 오른쪽 앞 뒤
riped = []
unriped_exist = False
visited = [[[0 for m in range(M)] for n in range(N)] for h in range(H)]
for h in range(H):
    temp = []
    for n in range(N):
        temp2 = list(map(int, sys.stdin.readline().rstrip().split()))
        for m in range(M):
            if temp2[m] == 1:
                riped.append([h, n, m])
            if temp2[m] == 0:
                unriped_exist = True
            if temp2[m] == -1:
                visited[h][n][m] = -1
        temp.append(temp2)
    box.append(temp)
# print(box, riped, box[riped[0][0]][riped[0][1]][riped[0][2]])
# print(visited)


def bfs(Vs):
    dq = deque()
    for v in Vs:
        dq.append(v)
        visited[v[0]][v[1]][v[2]] = 1

    while dq:
        h, n, m = dq.popleft()
        for a_h, a_n, a_m in affect:
            new_h = h + a_h
            new_n = n + a_n
            new_m = m + a_m
            if 0 <= new_h < H and 0 <= new_n < N and 0 <= new_m < M and box[new_h][new_n][new_m] != -1 and visited[new_h][new_n][new_m] == 0:
                dq.append([new_h, new_n, new_m])
                visited[new_h][new_n][new_m] = visited[h][n][m] + 1
if unriped_exist == False:
    print(0)
    exit(0)
bfs(riped)
# print(visited)
answer = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if visited[h][n][m] == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(visited[h][n]))
print(answer - 1)

# Python3: 60668KB	3328ms
# Pypy3: 220832KB	972ms