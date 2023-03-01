def get_ginsu(n,k):
    ginsu = ''
    while n:
        ginsu+=str(n%k)
        n = n//k
    return ginsu[::-1]

#     소수 확인하기
def sosu(num):
#     num의 제곱근 까지만 나눠지는 수가 있는지 확인하면 됨 -> 없으면 소수 !

    for i in range(2,int(num**(1/2))+1):
        if num%i==0:
            return False
    return True
    
def solution(n, k):
    result = 0
    ginsu = get_ginsu(n,k)
    print(ginsu.split('0'))
    for gs in ginsu.split('0'):
        # print(int(gs))
        # print(sosu(int(gs)))
        if (gs != '') and (int(gs) > 1) and (sosu(int(gs))):
            result+=1

    return result