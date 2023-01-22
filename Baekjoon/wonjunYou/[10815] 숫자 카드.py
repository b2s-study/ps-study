import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))
has_numbers = list(map(int, input().rstrip('\n').split()))

m = int(input().rstrip('\n'))
numbers = list(map(int, input().rstrip('\n').split()))

number_dic = {}

result = []

for has_number in has_numbers:
    number_dic[has_number] = 0

for number in numbers:
    if number not in number_dic:
        result.append(0)

    else:
        result.append(1)

print(*result)