# 2023. 1. 16
# 두수의 합

import sys

n = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline().rstrip())
# print(n, arr, x)

answer = 0

l, r = 0, n - 1
while l < r:
    temp = arr[l] + arr[r]
    if temp == x:
        answer += 1
        l += 1
    elif temp < x:
        l += 1
    elif temp > x:
        r -= 1

print(answer)

# 배열이 정렬된 상태에서 0번째 인덱스(l)와 n-1번째 인덱스(r)를 포인터로 가르키고 포인터를 이동하면서 두수의 합이 x인지를 판단한다.
# l에 따라서 r의 값을 조절하는 형태이다. r의 모든 경우의 수를 확인했다면, 새로운 케이스를 찾기위해 l을 오른쪽으로 이동시킨다.
# 두 포인터가 가르키는 값의 합이
# 같으면, answer += 1 하고, 새로운 케이스를 찾기 위해서 l를 오른쪽으로 이동시킨다.
# 작으면, l을 오른쪽으로 이동시킨다.
# 크면, r을 왼쪽으로 이동시킨다.
