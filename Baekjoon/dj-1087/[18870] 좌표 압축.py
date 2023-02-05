import sys

# ======================= init ======================= #

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))


# ======================= solve1 ======================= #
# 방안 1) 중복제거 후 이분 탐색
# 핵심 로직 - 이분 탐색, set()
'''
사전 작업: index값을 리턴하는 이분 탐색 함수 구현 - binary_search()
1. set()을 이용하여 리스트 X 안의 중복값 제거한 집합 생성 
2. 집합을 다시 리스트로 만들고 오름차순으로 정렬하여 리스트 sorted_X를 생성
3. for문으로 리스트 X의 값들을 순회하여 binary_search()로 sorted_X에서의 index값을 구함
4. index값은 0부터 시작이므로, 이는 곧 자기보다 작은 수의 갯수와 값이 같음 
'''


def binary_search(array, value):
    start, end = 0, len(array) - 1
    while (True):
        if start > end:
            break

        mid = (start + end) // 2
        if value < array[mid]:
            end = mid - 1
        elif value > array[mid]:
            start = mid + 1
        else:
            return mid
    return -1


sorted_X = list(set(X))
sorted_X.sort()
result = []
for value in X:
    count = binary_search(sorted_X, value)
    result.append(count)
print(*result)

# ======================= solve1 ======================= #
# 방안 2) 중복제거 후 dictionary 사용
# 핵심 로직 - dict(), set()
'''
1. set()을 이용하여 리스트 X 안의 중복값 제거한 집합 생성 
2. 집합을 다시 리스트로 만들고 오름차순으로 정렬하여 리스트 sorted_X를 생성
3. sorted_X의 요소들을 key=index, value=value로 dict()에 넣어 dict_X를 생성
4. for문으로 리스트 X의 값들을 순회하여 dict_X로 index값을 구함
5. index값은 0부터 시작이므로, 이는 곧 자기보다 작은 수의 갯수와 값이 같음 
'''

sorted_X = list(set(X))
sorted_X.sort()
dict_X = {}
for idx, value in enumerate(sorted_X):
    dict_X[value] = idx

for value in X:
    print(dict_X.get(value), end=" ")
