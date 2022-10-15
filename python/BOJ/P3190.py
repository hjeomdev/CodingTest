import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
board = [[0 for i in range(n)] for j in range(n)]  # 0 빈 공간, 1 뱀 ,2 사과

k = int(sys.stdin.readline().rstrip())
apple = []
for _ in range(k):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    i -= 1
    j -= 1
    board[i][j] = 2
    apple.append((i, j))
# print("apple", apple)

L = int(sys.stdin.readline().rstrip())
move = dict()
for _ in range(L):
    x, c = sys.stdin.readline().rstrip().split()
    x = int(x)
    move[x] = c
# print("move", move)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 동 북 서 남
direction = 0  # 방향 (시작은 오른쪽이라서 동)
x, y = 0, 0  # 현재 위치


def init():
    global board, x, y

    board = [[0 for v in range(n)] for t in range(n)]
    for idx in range(k):
        i, j = apple[idx]
        board[i][j] = 2
    x, y = 0, 0
    board[x][y] = 1


def turn(d):
    global direction

    if d == 'L':
        direction -= 1
    else:
        direction += 1

    if direction == -1:
        direction = 3
    elif direction == 4:
        direction = 0

    # if d == 'L':
    #     direction = (direction - 1) % 4
    # elif d == 'D':
    #     direction = (direction + 1) % 4

    # 문제를 잘못 이해하고 있었다.
    # 맨 처음에 오른쪽으로 움직인다는 말은 처음 방향에 대한 힌트였는데 마음대로 해석해서 읽고 있었다.


# 왜 -1 % 4 == 3 일까?
# https://betterprogramming.pub/modulo-operation-with-negative-numbers-in-python-38cb7256bb32
# https://www.geeksforgeeks.org/how-to-perform-modulo-with-negative-values-in-python/
# (a+b)mod n = [(a mod n)+(b mod n)]mod n

def solution():
    global x, y

    init()

    snake = deque()
    snake.append((x, y))
    count = 0

    while True:
        count += 1

        x += dx[direction]
        y += dy[direction]

        # 벽에 부딪힌 경우
        if x < 0 or x >= n or y < 0 or y >= n:
            break

        # 사과를 만난 경우
        if board[x][y] == 2:
            board[x][y] = 1
            snake.append((x, y))
        elif board[x][y] == 1:  # 자기 몸을 만난 경우
            break
        elif board[x][y] == 0:
            board[x][y] = 1
            snake.append((x, y))
            px, py = snake.popleft()
            board[px][py] = 0

        # 방향을 바꿔야 하는지 확인
        if count in move:
            turn(move[count])

    return count


print(solution())
# 참고1: https://hongcoding.tistory.com/127
# 참고2: https://velog.io/@hope1213/%EB%B0%B1%EC%A4%80-3190%EB%B1%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
