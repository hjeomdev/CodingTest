import sys

N = int(input())
A = list(map(int, input().split()))
# print(N, A)

# 1. 시간초과
# result = []
# for i in range(N):
#     def f(x):
#         return x > A[i]
#     temp = list(filter(f, A[i + 1:]))
#     if len(temp) == 0:
#         result.append("-1")
#     else:
#         result.append(str(temp[0]))
#
# print(' '.join(result))

# 2. 158196KB	1312ms (python3),	274736KB	532ms(pypy3)
# 배열이 엄청 길기 때문에 1회 순회할 때 모든 것을 확인 해야한다

stack = [0]
result = [-1] * N
for i in range(1, N):
    if A[stack[-1]] >= A[i]:
        stack.append(i)
    else:
        while A[stack[-1]] < A[i]:
            idx = stack.pop()
            result[idx] = A[i]
            if len(stack) == 0:
                break
        stack.append(i)

print(' '.join(list(map(lambda x: str(x), result))))
