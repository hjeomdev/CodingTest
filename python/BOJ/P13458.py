import sys

N = int(sys.stdin.readline().rstrip())  # 시험장 개수
A = list(map(int, sys.stdin.readline().rstrip().split()))  # 각 시험자의 응시자 수
B, C = map(int, sys.stdin.readline().rstrip().split())  # 총감독관이 감시할 수 있는 응시자 수, 부감독관이 감시할 수 있는 응시자 수
# print(N, A, B, C)

answer = 0

for i in range(N):
    taker = A[i]

    answer += 1  # 총감독관은 최대 한 명
    taker -= B
    # print(taker, answer)

    if taker > 0:
        answer += taker // C
        taker = taker % C
        if taker > 0:
            answer += 1

print(answer)

# 149432KB	968ms
