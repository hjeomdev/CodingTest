import sys

n = int(sys.stdin.readline().rstrip())

nums = list(map(int, sys.stdin.readline().rstrip().split()))
# print(n, nums)

sum = [0] * n
sum[0] = nums[0]
for i in range(1, n):
    # sum[i] = max(sum[i - 1], sum[i - 1] + nums[i], nums[i]) 연속되어야 하기 때문에 불가능
    sum[i] = max(nums[i], sum[i - 1] + nums[i])
# print(sum)
print(max(sum))
