import sys

# dict를 이용한 풀이 O(nlogn + n)

input = sys.stdin.readline

n = int(input().rstrip('\n'))

numbers = list(map(int, input().rstrip('\n').split()))

new_numbers = list(set(numbers))
new_numbers.sort()

number_idx = dict()

for idx in range(len(new_numbers)):
    number_idx[new_numbers[idx]] = idx

for number in numbers:
    print(number_idx[number], end=" ")

''' 이분 탐색 풀이 : O(nlogn + nlogn)
import sys

input = sys.stdin.readline

def find_index(target, new_numbers):
    start = 0
    end = len(new_numbers) - 1

    while (start <= end):
        mid = (start + end) // 2

        if new_numbers[mid] == target:
            return mid

        if new_numbers[mid] > target:
            end = mid - 1

        if new_numbers[mid] < target:
            start = mid + 1

    return 0

n = int(input().rstrip('\n'))

numbers = list(map(int, input().rstrip('\n').split()))

new_numbers = list(set(numbers))
new_numbers.sort()

result = []
for number in numbers:
    result.append(find_index(number, new_numbers))

print(*result)
'''