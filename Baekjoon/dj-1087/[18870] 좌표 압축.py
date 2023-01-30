import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
unique_X = list(set(X))
unique_X.sort()
sorted_X = enumerate(unique_X)
dict_X = {}
for idx, value in sorted_X:
    dict_X[value] = idx

for value in X:
    print(dict_X.get(value), end=" ")
