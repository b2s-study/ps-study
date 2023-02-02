import sys

input = sys.stdin.readline

def deduplicate(numbers):
    arr = []
    arr.append(numbers[0])

    for idx in range(1, len(numbers)):
        if (numbers[idx] != numbers[idx - 1]):
            arr.append(numbers[idx])

    return arr

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

new_numbers = deduplicate(sorted(numbers))

result = []
for number in numbers:
    result.append(find_index(number, new_numbers))

print(*result)
