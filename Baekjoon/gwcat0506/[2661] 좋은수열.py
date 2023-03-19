
# 미완성
# 숫자 1, 2, 3으로만 이루어지는 수열
import sys

n = int(sys.stdin.readline())

def bad_seq(num):
    # 체크하는 방법???
    
    
def dfs(num):
    global n
    
    if len(num) == n:
        print(num)
        # 어차피 Minimum이기 때문에 바로 exit(코드종료) 해준다.
        exit()
        
    for i in '123':
        if bad_seq(num + str(i)):
            dfs(num + str(i))
    return

dfs('1')
