
# 실패 -> 다시 풀기 

import sys

input = sys.stdin.readline

n = int(input())
paper = []
for _ in range(n):
    n_list = list(map(int,input().split(" ")))
    paper.append(n_list)
    
    
def paper_check(num1,num2,num3,num4):
    global white_cnt
    global blue_cnt
    
    white = 0
    blue = 0
    
    print("1",num1,num2+1)
    print("2",num3,num4+1)
    
    for i in range(num1,num2):
        for j in range(num3,num4):
            if paper[i][j]==0:
                white+=1
                continue
            blue+=1
    # 모든 색종이가 white이면
    if white == (num2-num1)*(num4-num3):
        white_cnt+=1
        return white_cnt
    elif blue == (num2-num1)*(num4-num3):
        blue_cnt+=1
        return blue_cnt
    else:
        # section 1
        # 0 4 0 4
        paper_check(num1,num2//2,num1,num2//2)
        # section 2
        # 5 8 0 4
        paper_check(num2//2,num2,num3,num4//2)
        # section 3
        paper_check(num1,num2//2,num4//2,num4)
        # section 4
        paper_check(num2//2,num2,num4//2,num4)
        
    
white_cnt = 0
blue_cnt = 0 
 
print(paper_check(0,n,0,n))