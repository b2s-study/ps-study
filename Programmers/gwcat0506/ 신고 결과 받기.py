
def solution(id_list, report, k):
    
    dic = {}
    
    for rep in report:
        user, rep_user = rep.split(' ')
        if not rep_user in dic:
            dic[rep_user] = [user]
            continue
#         중복 방지
        if not user in dic[rep_user]:
            dic[rep_user].append(user)
#     dic -> 신고 받은 사람 : 신고한 사람   
    # print(dic)
    
    
    result = [0]*len(id_list)
    for id in dic:
        if len(dic[id])>=k:
            for user in dic[id]:
                result[id_list.index(user)]+=1
        
    return result