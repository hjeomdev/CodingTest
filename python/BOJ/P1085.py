import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

rectangle = [h - y, y, x, w - x] # 상 하 좌 우

sys.stdout.write(str(min(rectangle)))