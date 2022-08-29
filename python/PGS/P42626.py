import heapq


def solution(scoville, K):
    answer = 0

    h = []
    for i in scoville:
        heapq.heappush(h, i)

    while h[0] < K:
        answer += 1
        item = heapq.heappop(h)
        item2 = heapq.heappop(h)
        heapq.heappush(h, item + (item2 * 2))

        if len(h) == 1 and h[0] < K:
            return -1

    return answer

# [힙큐](https://docs.python.org/ko/3/library/heapq.html)
# heapq.heappush(heap, item)

# heapq.heappop(heap): 힙이 비어 있으면, IndexError가 발생합니다. 팝 하지 않고 가장 작은 항목에 액세스하려면, heap[0]을 사용하십시오.

# heapq.heapify(x): 리스트 x를 선형 시간으로 제자리에서 힙으로 변환합니다.

# heapq.heappushpop(heap, item): 푸시 후에 팝. push와 pop을 별도로 호출하는 것보다 더 효율적으로 실행합니다.

# heapq.heapreplace(heap, item): 팝 후에 푸시. 힙이 비어 있으면, IndexError가 발생합니다. pop와 push을 별도로 호출하는 것보다 더 효율적으로 실행합니다.

# heapq.merge(*iterables, key=None, reverse=False): 정렬된 값에 대한 이터레이터를 반환합니다.
# sorted(itertools.chain(*iterables))와 비슷하지만 이터러블을 반환하고, 데이터를 한 번에 메모리로 가져오지 않으며, 각 입력 스트림이 이미 (최소에서 최대로) 정렬된 것으로 가정합니다.
# key는 각 입력 요소에서 비교 키를 추출하는 데 사용되는 단일 인자의 키 함수를 지정합니다. 기본값은 None입니다 (요소를 직접 비교합니다).

# heapq.nlargest(n, iterable, key=None): iterable에 의해 정의된 데이터 집합에서 n 개의 가장 큰 요소로 구성된 리스트를 반환합니다.
# key가 제공되면 iterable의 각 요소에서 비교 키를 추출하는 데 사용되는 단일 인자 함수를 지정합니다 (예를 들어, key=str.lower). 다음과 동등합니다: sorted(iterable, key=key, reverse=True)[:n].
#
# heapq.nsmallest(n, iterable, key=None)
# iterable에 의해 정의된 데이터 집합에서 n 개의 가장 작은 요소로 구성된 리스트를 반환합니다.
# key가 제공되면 iterable의 각 요소에서 비교 키를 추출하는 데 사용되는 단일 인자 함수를 지정합니다 (예를 들어, key=str.lower). 다음과 동등합니다: sorted(iterable, key=key)[:n].
#
# 마지막 두 함수는 작은 n 값에서 가장 잘 동작합니다. 값이 크면, sorted() 기능을 사용하는 것이 더 효율적입니다.
# 또한, n==1일 때는, 내장 min()과 max() 함수를 사용하는 것이 더 효율적입니다. 이 함수를 반복해서 사용해야 하면, iterable을 실제 힙으로 바꾸는 것이 좋습니다.