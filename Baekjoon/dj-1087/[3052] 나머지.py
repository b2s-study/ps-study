import sys

input = sys.stdin.readline

repeat = 10
result_set = set()

for _ in range(repeat):
  number = int(input())
  result = number % 42
  result_set.add(result)

print(len(result_set))