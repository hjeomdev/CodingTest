import sys

n = int(sys.stdin.readline().rstrip())
road = list(map(int, sys.stdin.readline().rstrip().split()))
price = list(map(int, sys.stdin.readline().rstrip().split()))
# print(n, road, price)

# hoarding_point = price.index(min(price))
#
# answer = 0
# for i in range(len(price)):
#     # print(answer)
#     if i == hoarding_point:
#         # print('left', sum(road[i:]))
#         answer += price[i] * sum(road[i:])
#     else:
#         answer += price[i] * road[i]
# 뭔가 착각함...

answer = 0
i = 0
while i < n - 1:
    gas = road[i]  # 바로 다음 마을까지 필요한 양
    to = i + 1  # 현재 충전한 가스로 최대한 갈 수 있는 곳
    for j in range(i + 1, n - 1):  # 바로 앞 마을 부터 마지막 그 전 마을 까지 가스 가격을 비교
        if price[i] <= price[j]:
            gas += road[j]
            to += 1
        else:
            break
    answer += gas * price[i]
    # print(i, answer, gas)
    i = to

sys.stdout.write(str(answer))

# 45388KB	344ms

# 5
# 3 2 1 4
# 5 8 9 4 1
# answer: 46