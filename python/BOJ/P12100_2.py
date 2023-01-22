import sys
from collections import deque
import copy

n = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
# print(n, matrix)

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 상 좌 하 우


def print_matrix(a, b, c, d, e):
    print(a, b, c, e)
    for k in range(n):
        print(d[k])
    print()


def move(board, direct):
    b = copy.deepcopy(board)

    if direct == d[0]:
        for j in range(n):
            top = 0
            for i in range(1, n):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0
                    if b[top][j] == 0:
                        b[top][j] = temp
                    elif b[top][j] == temp:
                        b[top][j] *= 2
                        top += 1
                    else:
                        top += 1
                        b[top][j] = temp
                # print_matrix(i, j, top, b, direct)
    elif direct == d[1]:
        for i in range(n):
            top = 0
            for j in range(1, n):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0
                    if b[i][top] == 0:
                        b[i][top] = temp
                    elif b[i][top] == temp:
                        b[i][top] *= 2
                        top += 1
                    else:
                        top += 1
                        b[i][top] = temp
    elif direct == d[2]:
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0
                    if b[top][j] == 0:
                        b[top][j] = temp
                    elif b[top][j] == temp:
                        b[top][j] *= 2
                        top -= 1
                    else:
                        top -= 1
                        b[top][j] = temp
    elif direct == d[3]:
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0
                    if b[i][top] == 0:
                        b[i][top] = temp
                    elif b[i][top] == temp:
                        b[i][top] *= 2
                        top -= 1
                    else:
                        top -= 1
                        b[i][top] = temp
    return b


def bfs():
    dq = deque()

    answer = 0

    dq.append([copy.deepcopy(matrix), 0])

    while dq:
        m, depth = dq.popleft()

        if depth >= 5:
            temp = 0
            for t in range(n):
                temp = max(temp, max(m[t]))
            answer = max(answer, temp)
            continue

        for k in range(len(d)):
            new_m = move(m, d[k])
            dq.append([copy.deepcopy(new_m), depth + 1])

    return answer


print(bfs())

# 두번째 푸는 거지만 여전히 제 힘으로 못 풀었다.
# 최대 5번 움직이기 때문에 4 * 4 * 4 * 4 * 4 = 1024가지의 경우의 수만 확인하면 되기 때문에 브루트포스로 풀면된다.
# 는건 파악을 했다.
# 문제는 구현파트였다. 카드가 합해지는 규칙이 구현하기 너무 어려웠다.
# 분명 패턴이 있어서 나름 조건식을 세워봤는데, 놓치는 부분이 있었다.
# 정답을 읽고 내가 이해한 만큼 설명해보자면,
# 방향이 상하면 열을 기준으로 행을 순회하고, 좌우면 행을 기준으로 열을 순회한다.
# 그래서 어떤 방향이던 행과 열을 순회하는 이중 for문이 있다.
# 값을 입력할 곳을 표시하는 top 변수가 있고, 만약 상으로 이동할 경우 j를 기준으로 i를 순회한다.
# i가 가르키는 곳에 값이 있다면 (0 이상이라면) top이 가르키는 곳이 어떤 값을 가지고 있는지 확인한다.
# top == 0 이면, top에다 i가 가르키는 값을 그대로 옮기고 top의 위치는 유지한다.
# 왜냐하면, i 뒤에 i가 가르키는 값과 같은 값이 있을 수 있기 때문이다.
# top == matrix[i][j] 이면, top이 가르키는 값을 두배로 만들고 i가 가르키는 값을 0으로 만든다.
# 왜냐하면, 합쳐지는 경우이기 때문이다.
# top이 0도, matrix[i][j]도 아니라면, top의 위치를 +1하고 거기에 i의 값을 저장한다.
# 왜냐하면 새로운 값이므로 다음 칸에 저장해야하기 때문이다.
# 이해는 나름 한거 같은데 다음에도 구현을 할 수 있을지 의문이다. 휴.
