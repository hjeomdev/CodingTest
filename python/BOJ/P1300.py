import sys

input = sys.stdin.readline

N = int(input().rstrip())
k = int(input().rstrip())
# print(N, k)

# 1. 문제 파악 못함
# total = N * N
# x = k // N + 1
# y = k % N + 1
# print(x * y)

# 오름차순 정렬을 해야한다고...! 문제 제대로 읽자!

# 2. 30840KB	1144ms -> 30840KB	992ms (범위를 1 - k로 줄여서 시간을 줄임)
# N이 최대 10000이니 N * N은 십억이다.. 그러므로 직접 만들어서 오름차순으로 구하기는 비효율적이다.
# 이분탐색 카테고리에 속한 문제답게 이분탐색으로 풀려고 하는데, 찾은 수가 답인지 확인하는 조건문을 어떻게 설정해야할지 모르겠다.

# mid 값을 구했을 때, 그 값보다 작은 수의 개수가 몇 개 인지(mid가 몇번째 숫자인지) 확인해야한다
# 근데 그걸 어떻게?

# https://velog.io/@uoayop/BOJ-1300-K%EB%B2%88%EC%A7%B8-%EC%88%98Python
# 이 글을 읽고 이해했다.

answer = 0
# start, end = 1, N * N
start, end = 1, k

while start <= end:
    mid = (start + end) // 2

    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)

    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)

