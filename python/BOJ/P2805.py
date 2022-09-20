import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))
# print(N, M, trees)

answer = 0

# 1. 시간초과, pypy3으로 제출하면 맞음(262760KB	524ms)
start, end = 1, max(trees)
while start <= end:
    mid = (start + end) // 2

    count = 0
    for t in trees:
        if t >= mid:
            count += t - mid

    if count >= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
