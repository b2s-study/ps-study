
# 풀이 1. 시간초과.. 
# stack으로 풀기  
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    
    functions = str(sys.stdin.readline()).rstrip()
    n = int(sys.stdin.readline())
    n_str = str(sys.stdin.readline())
    n_list = n_str[1:-2].split(',')
    
    reverse = 0
    
    # 배열이 비었을 경우 error 출력하게 만들기
    if n==0:
        n_list = []
    
    try:
        for fun in functions:
            # print('fun',fun)
            if fun == 'R':
                reverse+=1
                
            if fun == 'D': 
                # reverse가 짝수이면
                if reverse%2==0:
                    # 첫 번째 요소 slicing
                    n_list = n_list[1:]
                    continue
                # 홀수이면
                # 첫 번째 요소 pop
                n_list.pop()
                
        # 홀수이면 반대로 출력 
        if reverse%2!=0:  
            n_list.reverse()

        # 출력문 형식이 꼭 같은지 확인하기... 이것때매 틀렸다 ㅡㅡ
        print('[' + ",".join(n_list) + ']')  
    except:
        print('error')
        
        

# 풀이 2. deque 이용(정답)
        
import sys
from collections import deque
T = int(sys.stdin.readline())

for _ in range(T):
    
    functions = str(sys.stdin.readline()).rstrip()
    n = int(sys.stdin.readline())
    n_str = str(sys.stdin.readline())
    n_list = n_str[1:-2].split(',')
    
    # deque 만들기
    queue = deque(n_list)
    reverse = 0
    
    # 배열이 비었을 경우 error 출력하게 만들기
    if n==0:
        queue = deque()
    
    try:
        for fun in functions:
            # print('fun',fun)
            if fun == 'R':
                reverse+=1
                
            if fun == 'D': 
                # reverse가 짝수이면
                if reverse%2==0:
                    # 첫 번째 요소 slicing
                    queue.popleft()
                    continue
                # 홀수이면
                # 첫 번째 요소 pop
                queue.pop()
                
        # 홀수이면 반대로 출력 
        if reverse%2!=0:  
            queue.reverse()

        # 출력문 형식이 꼭 같은지 확인하기... 이것때매 틀렸다 ㅡㅡ
        print('[' + ",".join(queue) + ']')  
    except:
        print('error')
        

# 질문
# 첫 번째 요소 slicing
# n_list = n_list[1:]의 시간 복잡도가 큰지 얼마나 되는지