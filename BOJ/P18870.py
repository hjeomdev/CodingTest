import sys

N = int(sys.stdin.readline().rstrip())

# xs = list(map(int, sys.stdin.readline().rstrip().split()))
#
# xs_set = list(set(xs))
# xs_set.sort()
#
# for x in xs:
#     sys.stdout.write(str(xs_set.index(x)) + ' ')

# 시간 초과가 나서 질문 검색을 해보니 https://www.acmicpc.net/board/view/79136
# .index() 연산이 N번 실행되어 O(N^2)의 시간복잡도를 가지기때문에 나는 문제라는 것!
# 파이썬 라이브러리는 편하지만 시간복잡도를 가늠하기 어렵다..

xs = list(map(int, sys.stdin.readline().rstrip().split()))

xs_set = list(set(xs))
xs_set.sort()

xs_dict = { xs_set[i]:i for i in range(len(xs_set)) }
# x = { key : value for i in range(len(numbers)) } 이 표현이 너무 낯설다..

for i in xs:
    sys.stdout.write(str(xs_dict[i]) + ' ')
