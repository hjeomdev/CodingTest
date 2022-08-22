import sys

n = int(sys.stdin.readline().rstrip())
stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline().rstrip()))

dp = [0] * n

dp[0] = stairs[0]  # 첫번째 = 첫번째

# print(dp)
for i in range(1, n):
    if i == 1:
        dp[1] = stairs[0] + stairs[1]  # 두번째 = 첫번째 + 두번째
    elif i == 2:
        dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])  # 세번째 = 첫번째 + 세번째 or 두번째 + 세번째 -> 세 번 연달아 밟을 수 없니까
    else:
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    # i 번째 계단에 왔을 때 어떻게 왔는지 추리해보면,
    # 1안) i-3 번째 계단과 i-1 번째 계단을 밟고 왔다 (2칸 건너고, 1칸 건너고)
    # 2안) i-2 번째 계단을 밟고 왔다 (2칸 건너고)
    # 1칸 건너는 경우를 따지지 않는 이유는 그러면 i번째 계단은 3번 연속으로 밟게 되니까

print(dp[n - 1])
