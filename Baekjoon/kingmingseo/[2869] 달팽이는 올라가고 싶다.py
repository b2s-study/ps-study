import math
import sys
input= sys.stdin.readline

day , night , tree = map(int,input().split())

answer=(tree-night)/(day-night)

print(math.ceil(answer))