import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

u = []

def binary_search(target, u):
    start = 0
    end = len(u) - 1

    while (start <= end):
        mid = (start + end) // 2

        if u[mid] == target:
            return 1

        if u[mid] > target:
            end = mid - 1

        if u[mid] < target:
            start = mid + 1

    return 0

for _ in range(n):
    number = int(input().rstrip('\n'))
    u.append(number)

u.sort()

two_sum = []

for i in range(len(u)):
    for j in range(i, len(u)):
        two_sum.append(u[i] + u[j])

two_sum.sort()

checked = False
for i in range(len(u) - 1, 0, -1):
    for j in range(0, i):
        if (binary_search((u[i] - u[j]), two_sum)):
            checked = True
            print(u[i])
            break

    if checked:
        break