def solution(arr):
    answer = []

    # print(set(arr)) # set은 정렬을 한다.

    answer.append(arr[0])
    previous = arr[0]
    for i in range(1, len(arr)):
        if previous != arr[i]:
            previous = arr[i]
            answer.append(arr[i])

    return answer