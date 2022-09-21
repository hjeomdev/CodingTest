import sys

input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
# houses = []
# for _ in range(N):
#     houses.append(int(input().rstrip()))
houses = [int(input().rstrip()) for _ in range(N)]
# print(N, C, houses)

# 1. 38568KB	964ms
houses.sort()

answer = 0
start, end = 1, houses[-1]

while start <= end:
    # print('a', start, end)
    mid = (start + end) // 2
    count = 1
    previous = houses[0]

    for i in range(1, len(houses)):
        # print(houses[i], previous, mid, answer)
        if houses[i] - previous >= mid:
            previous = houses[i]
            count += 1
            # print(previous)

    if count >= C:
        answer = mid
        start = mid + 1
    elif count < C:
        end = mid - 1

print(answer)
