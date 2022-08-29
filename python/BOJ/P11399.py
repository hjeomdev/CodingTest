import sys

n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))
# print(n, p)

# p.sort()
# # print(p)
#
# temp = 0
# for i in range(len(p)):
#     p[i] += temp
#     temp = p[i]

# 아래 코드가 더 깔끔한거 같다.
result = 0  # 총합
temp = 0  # 누적합
for i in sorted(p):
    temp += i
    result += temp

print(result)
