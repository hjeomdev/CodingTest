import sys

T = int(sys.stdin.readline().rstrip())

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(dp[N]) + "\n")

# 개행문자 안 넣어서 두번이나 틀렸다... 바보다 진짜