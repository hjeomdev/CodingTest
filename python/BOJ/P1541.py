import sys

formula = sys.stdin.readline().rstrip().split('-')
# print(formula)

result = []
for i in formula:
    result.append(i.split('+'))

answer = sum(list(map(int, result[0])))
for i in range(1, len(result)):
    if len(result[i]) > 1:
        answer -= sum(list(map(int, result[i])))
    else:
        answer -= int(result[i][0])

print(answer)

# 30840KB	68ms