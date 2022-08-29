import sys

n = int(sys.stdin.readline().rstrip())
meeting = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    meeting.append([s, e])

meeting.sort(key=lambda x:[x[1], x[0]])
# print(meeting)

cnt = 1
end_time = meeting[0][1]
for i in range(1, n):
    if end_time <= meeting[i][0]:
        cnt += 1
        end_time = meeting[i][1]

sys.stdout.write(str(cnt))

# 54688KB	352ms

# 참조: https://suri78.tistory.com/26
# 문제를 해결하는 핵심문장은, "빨리 끝나는 미팅을 해야지 다른 미팅을 고려할 수 있다."는 거다.