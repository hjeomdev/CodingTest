from collections import deque


def solution(progresses, speeds):
    answer = []

    dq = deque()
    dq.append((progresses, speeds))

    while dq:
        pro, spe = dq.popleft()

        first_pro_need = (100 - pro[0]) // spe[0]
        rest = (100 - pro[0]) % spe[0]
        if rest > 0:
            first_pro_need += 1

        count = 0

        for i in range(len(pro)):
            pro[i] += first_pro_need * spe[i]

        for i in range(len(pro)):
            if pro[i] < 100:
                dq.append((pro[i:], spe[i:]))
                break
            else:
                count += 1

        answer.append(count)

    return answer
