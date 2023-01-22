import sys
from copy import deepcopy

N = int(sys.stdin.readline().rstrip())
b = []
for _ in range(N):
    b.append(list(map(int, sys.stdin.readline().split())))
# print(b)


def up(plate):
    # 위
    for j in range(N):
        t = 0
        for i in range(1, N):
            if plate[i][j]:
                temp = plate[i][j]
                plate[i][j] = 0

                if plate[t][j] == 0:  # 위가 0이면 옮긴다
                    plate[t][j] = temp
                elif plate[t][j] == temp:  # 위가 같은 수면 더한다
                    plate[t][j] *= 2
                    t += 1
                else:  # 위가 0도 아니고 같은 수도 아니라면
                    t += 1
                    plate[t][j] = temp  # 원래 있던 자리에 저장
    # 확인할 값을 위는 a, 아래는 b라고 할 때, 값이 바뀐다면 b가 이동할 가능성이 높다.
    # 그러므로 b의 값을 임시로 저장하고 그 자리에 0을 넣어 둔 뒤, a의 값을 확인한다.
    # 1. a == 0, b를 a의 자리로 이동
    # 2. a == b, a + b값을 a에 저장
    # 3. a가 다른 수인 경우, 그대로 유지한다.
    # 이때, 현재 확인하는 원소의 인덱스(i), 지금 확인한 값을 넣을 인덱스(a, t)를 계속 관리하면서 반복하면 된다.
    # 1번째 상황인 경우에는 1개의 원소만 확인한 상태여서 다음에 오는 값에 따라 값이 달라질 수 있기 때문에(값이 수정될 수 있기 때문에) t는 변경되지 않지만,
    # 2, 3번째인 경우에는 t에 2개의 원소를 확인한, 확정적인 값이 채워졌기 때문에 t += 1이 수행된다.
    return plate


def down(plate):
    for j in range(N):
        t = N - 1
        for i in range(N - 2, -1, -1):
            if plate[i][j]:
                temp = plate[i][j]
                plate[i][j] = 0

                if plate[t][j] == 0:  # 아래가 0이면 옮긴다
                    plate[t][j] = temp
                elif plate[t][j] == temp:  # 아래가 같은 수면 더한다
                    plate[t][j] *= 2
                    t -= 1
                else:  # 아래가 0도 아니고 같은 수도 아니라면
                    t -= 1
                    plate[t][j] = temp
    return plate


def left(plate):
    for i in range(N):
        t = 0
        for j in range(1, N):
            if plate[i][j]:
                temp = plate[i][j]
                plate[i][j] = 0

                if plate[t][j] == 0:
                    plate[t][j] = temp
                elif plate[t][j] == temp:
                    plate[t][j] *= 2
                    t += 1
                else:
                    t += 1
                    plate[t][j] = temp
    return plate


def right(plate):
    for i in range(N):
        t = N - 1
        for j in range(N - 2, -1, -1):
            if plate[i][j]:
                temp = plate[i][j]
                plate[i][j] = 0

                if plate[i][t] == 0:
                    plate[i][t] == temp
                elif plate[i][t] == temp:
                    plate[i][t] *= 2
                    t -= 1
                else:
                    t -= 1
                    plate[i][t] = temp
    return plate

answer = 0
def dfs(B):
    global answer
    stack = [(deepcopy(B), 0)]

    while stack:
        print(stack)
        board, depth = stack.pop()

        if depth == 5:
            for i in range(N):
                answer = max(answer, max(board[i]))
                print(answer)
            continue

        stack.append((up(deepcopy(board)), depth + 1))
        stack.append((down(deepcopy(board)), depth + 1))
        stack.append((left(deepcopy(board)), depth + 1))
        stack.append((right(deepcopy(board)), depth + 1))


dfs(b)
print(answer)
