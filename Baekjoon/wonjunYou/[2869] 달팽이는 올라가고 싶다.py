import sys
import math

input = sys.stdin.readline

A, B, V = map(int, input().rstrip('\n').split())

days = math.ceil((V - A) / (A - B)) + 1

print(days)