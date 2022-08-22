# 전혀 모르겠어서 검색.. https://zidarn87.tistory.com/272
# 모든 경우의 수를 연속합으로 구하는 것 같다
import sys

n = int(sys.stdin.readline().rstrip())

dp = []

for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, len(dp)):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]

sys.stdout.write(str(min(dp[n - 1])))

# 1초 정도 걸리는 거 같아서 틀린 줄 알았는데 맞았다..
# R을 쓰려면 앞집에서 G or B 중에 가장 작은 걸로 골라야 하고 그 결과를 계속 누적 시킬 생각을 못했다