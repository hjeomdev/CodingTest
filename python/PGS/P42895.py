def solution(N, number):
    answer = -1

    #     number = 2
    #     N = 1, 2
    #     N = 2, (2+2), 2-2, 2/2, 2*2, 22
    #     N = 3, (2+2+2), ..., (2+2*2), ..., 22+2, ... 22*2, 222
    #       ...
    #     => N=2인 집합의 각 원소에 사칙연산을 해서 나오는 경우들이 N=3인 집합에 포함된다.
    #     -> 아니다. N=1이라서 N=2인 집합에 사칙연산만 해도 원하는 결과가 나왔기 때문에 착각했다.
    #       N=5인 경우에, N=4인 집합에 사칙연산을 하면 원하는 결과도 나오지만,  (2+2+2+2)+2
    #       N=2인 집합과 N=3인 집합의 연산도 포함되어야 한다는 것을 놓쳤다. (2+2)+(2+2+2)

    max_N = 8

    dp = [set() for _ in range(max_N + 1)]
    dp[1].add(N)

    if N == number:
        return 1

    # for i in range(2, max_N + 1):
    #     dp[i].add(int(str(N) * i))  # 22, 222, 2222 와 같은 완전히 새로운 값을 저장하기 위함
    #     for j in dp[i-1]:
    #         dp[i].add(j + N)
    #         dp[i].add(j - N)
    #         if j != 0:
    #             dp[i].add(j // N)
    #         dp[i].add(j * N)
    #     print(i, dp[i])
    #     if number in dp[i]:
    #         print(number)
    #         answer = min(answer, i)

    for i in range(2, max_N + 1):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                    dp[i].add(num1 * num2)

        if number in dp[i]:
            return i

    return answer
