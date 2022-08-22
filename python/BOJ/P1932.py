import sys

n = int(sys.stdin.readline().rstrip())
triangle = [0] * n
for i in range(n):
    triangle[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    # print(triangle[i])
    if i > 0:
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    # print(triangle[i])

# print(n, triangle)
sys.stdout.write(str(max(triangle[n - 1])))

# 트리구조를 배열로 나타냈을 때, 자식노드가 부모노드에 접근하는 방법
# 자식노드가 (i, j)일 때, 왼쪽 대각선 부모는 (i-1, j-1)이고 오른쪽 대각선 부모는 (i-1, j)이다.
# 단, 트리의 한 레벨의 양 끝에 있는 노드들은 부모가 하나뿐인데, j가 0 이면 부모는 (i-1, j)이고, j가 마지막이면 (i-1, j-1)이다.