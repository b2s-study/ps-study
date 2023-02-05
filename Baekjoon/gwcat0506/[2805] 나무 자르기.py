
import sys

N,M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

# [중요]sort 필요없음
# trees.sort()

start = 0
end = max(trees)
while start<=end:
    
    mid = (start+end)//2
    
    target = 0
    
    for tree in trees:
        if tree <= mid:
            target+=0
        else:
            target += (tree-mid)
            
    if M <= target:
        start = mid+1
    else:
        end = mid-1
        
print(end)
    