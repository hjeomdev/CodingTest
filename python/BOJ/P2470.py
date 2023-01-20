# 2023. 1. 16
# 두 용액

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
# print(n, arr)

arr.sort()

l, r = 0, n - 1

diff = abs(arr[l] + arr[r])
answer = [arr[l], arr[r]]

while l < r:
    # 0에 가까운 수를 찾기 위해서 포인터가 움직일 때마다 값을 비교해 본다.
    temp = abs(arr[l] + arr[r])
    if temp < diff:
        diff = temp
        answer[0] = arr[l]
        answer[1] = arr[r]

    # 범위 조절 (포인터 이동)
    # 포인터의 합이 양수면 0에 가까워지도록 줄여야 하므로 오른쪽 포인터를 왼쪽으로 옮기고,
    # 포인터의 합이 음수면 0에 가까워지도록 늘여야 하므로 왼쪽 포인터를 오른쪽으로 옮긴다.
    if arr[l] + arr[r] > 0:
        r -= 1
    else:
        l += 1

print(' '.join(map(str, sorted(answer))))
