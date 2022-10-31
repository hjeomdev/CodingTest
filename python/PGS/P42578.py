def solution(clothes):
    answer = 0

    closet = dict()
    for i in range(len(clothes)):
        name, kind = clothes[i]
        if kind in closet:
            closet[kind].append(name)
        else:
            closet[kind] = [name]

    total = 1
    for i in closet.keys():
        total *= len(closet[i]) + 1  # 안 입는 경우를 추가하기 위해서 +1

    answer = total - 1  # 어떤 옷이던 안 입는 경우 제거하기 위해서 -1

    return answer