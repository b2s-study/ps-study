import sys

def Color(x,y,n):
    global white,blue     
    check=Mat[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=Mat[i][j]:     #나머지 사각형의 색깔과 일치하지 않는다면 실행
                Color(x,y,n//2)            #1사분면
                Color(x,y+n//2,n//2)       #2사분면
                Color(x+n//2,y,n//2)       #3사분면
                Color(x+n//2,y+n//2,n//2)  #4사분면
                return

    if check==0:
        white+=1
        return
    else:
        blue+=1
        return

input = sys.stdin.readline

N=int(input())
Mat=[list(map(int,input().split())) for _ in range(N)]

white,blue=0,0

Color(0,0,N)

print(white)
print(blue)