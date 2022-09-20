import sys

input = sys.stdin.readline

K, N = map(int, input().rstrip().split())

lines = []
for _ in range(K):
    lines.append(int(input().rstrip()))

# print(K, N, line)

# 1. 30840KB	116ms -> 100ms
start, end = 1, max(lines)
answer = 0
while start <= end:
    mid = (start + end) // 2

    # count = 0
    # for line in lines:
    #     count += line // mid
    count = sum([x // mid for x in lines])  # 이걸로 수정했더니 100ms로 줄어듦

    if count >= N:
        answer = mid
        start = mid + 1
    elif count < N:
        end = mid - 1

print(answer)
