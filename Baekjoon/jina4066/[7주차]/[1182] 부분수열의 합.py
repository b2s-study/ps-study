import sys

input = sys.stdin.readline

n, s = map(int, input().rstrip('\n').split())
lst = list(map(int, input().rstrip('\n').split()))
ans = []
count = 0

def solve(start):
    global count

    if sum(ans) == s and len(ans) > 0:
        count += 1
    
    for i in range(start, n):
        ans.append(lst[i])
        solve(i + 1)
        ans.pop()

solve(0)
print(count)