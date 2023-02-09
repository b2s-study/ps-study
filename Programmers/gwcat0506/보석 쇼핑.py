# 하다 말았음. -> 다시 풀기 

def check_gems(dic):
    for gem, cnt in dic:
        if cnt==0:
            return False
    return True

def solution(gems):
#     전체 보석의 종류 수 cnt
    gem_cnt = set(gems)
    p1 = 0
    p2 = 0
    
#   딕셔너리 만들기
    # {'SAPPHIRE': 0, 'DIA': 0, 'EMERALD': 0, 'RUBY': 0}
    
    while p1<=p2:
        cur_cnt = len(set(gems[p1:p2+1]))
        if cur_cnt == len(gem_cnt):
            dic = {gem : 0 for gem in set(gems[p1:p2+1])}
            for gem, cnt in dic:
                for gem in gems[p1:p2+1]:
                    dic[gem]+=1
            if check_gems(dic):
        #         p1을 늘려도 보석의 unique 갯수가 똑같으면 p1을 늘려도 됨

                while True:
                    if  cur_cnt == len(set(gems[p1+1:p2+1])):
                        p1+=1
                    else:
                        break
                
                return [p1,p2]
        p2+=1
    
    