import sys
from collections import deque

T = 1
while True:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        tree[v1].append(v2)
        tree[v2].append(v1)

    print("tree", tree)

    # 트리가 되는 조건: 사이클이 없다 -> 그래프의 각 노드를 시작으로 트리를 훑으면서 사이클 여부를 확인해야 한다.
    visited = [False] * (n + 1)
    answer = 0


    def is_tree(graph, start):
        result = True
        dq = deque()
        dq.append(start)
        while dq:
            cur = dq.popleft()
            if visited[cur]:
                result = False
            visited[cur] = True
            for nex in graph[cur]:
                if not visited[nex]:
                    dq.append(nex)
        return result


    for i in range(1, n + 1):
        if not visited[i]:
            if is_tree(tree, i):
                answer += 1


    def print_test_result():
        print("Case ", T, ": ", sep='', end="")
        if answer == 0:
            print("No trees.")
        elif answer == 1:
            print("There is one tree.")
        else:
            print("A forest of", answer, "trees.", sep=' ')


    print_test_result()
    T += 1
