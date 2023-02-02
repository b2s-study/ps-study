import sys

input = sys.stdin.readline

def find_start(target, numbers):
    start = 0
    end = len(numbers)

    while (start < end):
        mid = (start + end) // 2

        if numbers[mid] >= target:
            end = mid

        else:
            start = mid + 1

    return start

def find_end(target, numbers):
    start = 0
    end = len(numbers)

    while (start < end):
        mid = (start + end) // 2

        if numbers[mid] > target:
            end = mid

        else:
            start = mid + 1

    return end

n = int(input().rstrip('\n'))
numbers = list(map(int, input().rstrip('\n').split()))

numbers.sort()

m = int(input().rstrip('\n'))
target_numbers = list(map(int, input().rstrip('\n').split()))

result = []

for target in target_numbers:
    start_idx = find_start(target, numbers)
    end_idx = find_end(target, numbers)

    result.append(end_idx - start_idx)

print(*result)