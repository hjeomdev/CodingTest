import sys

K = int(sys.stdin.readline().rstrip())
for k in range(K):
    V, E = map(int, sys.stdin.readline().rstrip().split())

    graph = [[] for _ in range(V + 1)]
    for e in range(E):
        u, v = map(int, sys.stdin.readline().rstrip().split())
        graph[u].append(v)
        graph[v].append(u)

    # print(graph)


    def dfs(R):  # E의 상태가 0이면 미방문, 1이면 방문했고 색칠함, 2이면 방문했고 색칠 안 함
        stack = [R]
        visited[R] = 1

        while stack:
            current = stack.pop()

            for n in graph[current]:
                # 연결된 노드 중에 색이 같은 노드가 있는지 확인한다
                if visited[n] == visited[current]:
                    return False

                # 연결된 노드를 확인한다
                if visited[n] == 0:
                    stack.append(n)
                    visited[n] = 2 if visited[current] == 1 else 1

        return True


    visited = [0 for _ in range(V + 1)]
    answer = ''
    for i in range(1, V + 1):
        if visited[i] == 0:
            if not dfs(i):
                answer = 'NO'
                break

    if answer == '':
        answer = 'YES'

    print(answer)
    # print(visited)

# 50548KB	1600ms