import sys

n = int(sys.stdin.readline().rstrip())

wine = []
for _ in range(n):
    wine.append(int(sys.stdin.readline().rstrip()))
# print(wine)

dp = [0] * n

visited = [False] * n

