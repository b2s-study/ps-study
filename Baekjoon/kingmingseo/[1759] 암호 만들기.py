import sys
input = sys.stdin.readline

L, C = map(int,input().split())
data = list(input().split())
data.sort()
arr = [0 for _ in range(L)]
isused = [False for _ in range(C)]
dic = {'a':1, 'b':2, 'c':3 ,'d':4, 'e':5 , 'f': 6, 'g':7 , 'h':8, 'i':9 , 'j':10 , 'k':11 , 'l' :12 , 'm' :13 , 'n':14 ,
       'o':15 , 'p':16 , 'q':17 , 'r':18, 's':19 ,'t':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26 , 0 : 0}
def func(k):
    if k == L :
        vo = 0
        co = 0
        for i in range(L):
            if arr[i] in 'aeiou':
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2:
            for i in range(L):
                print(arr[i],end='')
            print()
            return
        else:
            return

    for i in range(C):
        if isused[i] == False and (dic[arr[k-1]] < dic[data[i]] or k == 0):
            arr[k] = data[i]
            isused[i] = True
            func(k+1)
            isused[i] = False

func(0)





