import sys

input = sys.stdin.readline

N = int(input())

number_list = list(map(int, input().split()))
number_list.sort()
print(number_list[0], number_list[-1])