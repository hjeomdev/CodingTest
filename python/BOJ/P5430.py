# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
# for _ in range(T):
#     p = input().rstrip()
#
#     n = int(input().rstrip())
#
#     nums = input().rstrip().replace('[', '').replace(']', '')
#     if n > 1:
#         nums = list(map(int, nums.split(',')))
#     elif n == 1:
#         nums = [int(nums)]
#     elif n < 1:
#         nums = []
#
#     idx = 'l'
#     left = 0
#     right = len(nums) - 1
#     result = True
#     # print(nums, left, right)
#
#     for i in range(len(p)):
#         if p[i] == 'R':
#             idx = 'r' if idx == 'l' else 'l'
#         elif p[i] == 'D':
#             if len(nums) > 0:
#                 if idx == 'l':
#                     left += 1
#                 elif idx == 'r':
#                     right -= 1
#             else:
#                 result = False
#                 break
#     # print(left, right, idx)
#     if result and left <= right:
#         if idx == 'l':
#             print('[', ','.join(map(str, nums[left:right + 1])), ']', sep="")
#         elif idx == 'r':
#             print('[', ','.join(map(str, reversed(nums[left:right + 1]))), ']', sep="")
#     else:
#         print("error")

# 38684KB	3920ms

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().rstrip()

    n = int(input().rstrip())

    nums = input().rstrip().replace('[', '').replace(']', '')
    if n > 1:
        nums = list(map(int, nums.split(',')))
    elif n == 1:
        nums = [int(nums)]
    elif n < 1:
        nums = []

    idx = 'l'
    left = 0
    right = len(nums)
    result = True
    # print(nums, left, right)

    for i in range(len(p)):
        if p[i] == 'R':
            idx = 'r' if idx == 'l' else 'l'
        elif p[i] == 'D':
            if len(nums) > 0:
                if idx == 'l':
                    left += 1
                elif idx == 'r':
                    right -= 1
            else:
                result = False
                break
    # print(left, right, idx)
    if result and left <= right:
        if idx == 'l':
            print('[', ','.join(map(str, nums[left:right])), ']', sep="")
        elif idx == 'r':
            print('[', ','.join(map(str, reversed(nums[left:right]))), ']', sep="")
    else:
        print("error")

# 39860KB	356ms

# 배열을 실제로 삭제하지 않고 left, right 범위 인덱스와 방향 정보로 명령을 수행해서 10배 시간을 줄임 (오예!)
