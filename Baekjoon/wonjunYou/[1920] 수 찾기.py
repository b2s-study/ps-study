import sys

input = sys.stdin.readline

def find_number(target : int, numbers : list):
    start = 0
    end = len(numbers) - 1

    while (start <= end):
        mid = (start + end) // 2

        if numbers[mid] == target:
            return 1

        if numbers[mid] > target:
            end = mid - 1

        if numbers[mid] < target:
            start = mid + 1

    return 0

n = int(input().rstrip('\n'))
numbers = list(map(int, input().rstrip('\n').split()))

numbers.sort()

m = int(input().rstrip('\n'))
target_numbers = list(map(int, input().rstrip('\n').split()))

for target in target_numbers:
    print(find_number(target, numbers))