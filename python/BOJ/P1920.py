import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
qs = list(map(int, input().rstrip().split()))
# print(N, A, M, qs)

# 1.
# def binary_search(n, nums):
#     if len(nums) == 0:
#         print(0)
#         return 0
#
#     idx = len(nums) // 2
#     mid = nums[idx]
#
#     if n == mid:
#         print(1)
#         return 0
#     elif n < mid:
#         binary_search(n, nums[:idx])
#     elif mid < n:
#         binary_search(n, nums[idx + 1:])
#
# A.sort()
#
# for q in qs:
#     binary_search(q, A)

# 시간 초과..

# 2. 51024KB	224ms
d = {i : 1 for i in A}

# for q in qs:
#     if q in d:
#         print(1)
#     else:
#         print(0)

# 3. 49472KB	224ms
s = set(A)

for q in qs:
    if q in s:
        print(1)
    else:
        print(0)