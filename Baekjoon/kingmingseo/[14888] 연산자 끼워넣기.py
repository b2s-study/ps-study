import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
add , minus, mul, div = map(int,input().split())

max_result = -sys.maxsize
min_result = sys.maxsize

def func(k,arr):
    global add, minus, mul, div , max_result , min_result
    if k == N :
        max_result = max(max_result , arr)
        min_result = min(min_result , arr)
    else:
        if add > 0 :
            add = add - 1
            func(k+1, arr + data[k])
            add = add + 1

        if minus > 0 :
            minus = minus - 1

            func(k+1, arr - data[k])
            minus = minus + 1

        if mul > 0 :
            mul = mul - 1
            func(k+1, arr * data[k])
            mul = mul + 1

        if div > 0 :
            div  = div - 1
            func(k+1, int(arr / data[k]))
            div  = div + 1

func(1 , data[0])

print(max_result)
print(min_result)
