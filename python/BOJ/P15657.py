import sys
import itertools

n, m = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

num.sort()

arr = list(itertools.combinations_with_replacement(num, m))
arr.sort()
for a in arr:
    print(' '.join(map(str, a)))
