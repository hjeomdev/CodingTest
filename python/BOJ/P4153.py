import sys

nums = list(map(int, sys.stdin.readline().rstrip().split()))
while nums[0] != 0 and nums[1] != 0 and nums[2] != 0:
    nums.sort()
    # 직각삼각형의 피타고라스 정식 a^2 + b^2 = c^2 (c는 빗변)
    if nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
        sys.stdout.write("right\n")
    else:
        sys.stdout.write("wrong\n")
    nums = list(map(int, sys.stdin.readline().rstrip().split()))


