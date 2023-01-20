import sys
import itertools

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
# print(n, arr)

# x + y + z = k -> x + y = k - z

arr.sort()

# x + y 값을 모두 계산 (십만)
x_plus_y = set(x + y for x, y in list(itertools.product(arr, repeat=2)))
# print(x_plus_y)

# k - z가 x_plus_y 에 있는지 확인 (약 오만)
answer = 0
for k in range(n - 1, -1, -1):
    for z in range(k + 1):
        K = arr[k]
        Z = arr[z]
        if K - Z in x_plus_y:
            answer = max(K, answer)

print(answer)
