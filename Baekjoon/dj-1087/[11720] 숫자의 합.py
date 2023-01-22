import sys

input = sys.stdin.readline

N = int(input())
input_list = list(input())

number_list = list(map(int, input_list[0:N]))
print(sum(number_list))