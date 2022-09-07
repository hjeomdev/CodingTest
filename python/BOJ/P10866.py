import sys
input = sys.stdin.readline

N = int(input().rstrip())
dq = []

def isEmpty():
    if len(dq) > 0:
        return True
    else:
        return False

for i in range(N):
    command = input().rstrip().split()

    if command[0] == "push_front":
        dq.insert(0, int(command[1]))
    elif command[0] == "push_back":
        dq.append(int(command[1]))
    elif command[0] == "pop_front":
        if isEmpty():
            print(dq[0])
            dq = dq[1:]
        else:
            print(-1)
    elif command[0] == "pop_back":
        if isEmpty():
            print(dq[-1])
            dq = dq[:-1]
        else:
            print(-1)
    elif command[0] == "size":
        print(len(dq))
    elif command[0] == "empty":
        if isEmpty():
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if isEmpty():
            print(dq[0])
        else:
            print(-1)
    elif command[0] == "back":
        if isEmpty():
            print(dq[-1])
        else:
            print(-1)

# 30840KB	80ms

# 오... 명령문 확인하는 조건문에 배열의 길이가 0이상인지도 확인해서 0이상이 아니면 -1하도록 마지막에 default else문을 넣었음
# 오... 명령문을 등호로 확인한게 아니라 in 연산자로 확인한 사람도 있음