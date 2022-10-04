import sys


# 42024KB	900ms (python3), 186548KB	520ms (pypy3)
s = input()
bomb = input()
# print(s, bomb)
bomb_len = len(bomb)
result = []
for i in range(len(s)):
    result.append(s[i])
    if len(result) >= bomb_len:
        if ''.join(result[bomb_len * -1:]) == bomb:
            del result[bomb_len * -1:]
if len(result) == 0:
    print("FRULA")
else:
    print(''.join(result))
