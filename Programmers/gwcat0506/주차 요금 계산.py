import math
def calculator(in_time,out_time,basic_time,basic_fee,extra_time,extra_fee):
    if (out_time-in_time) <= basic_time:
        return basic_fee
    else:
        extra = math.ceil((out_time-in_time-basic_time)/extra_time)*extra_fee
        return basic_fee + extra
    
def solution(fees, records):
   # fees = [180, 5000, 10, 600]
    # print(fees)
    basic_time, basic_fee, extra_time, extra_fee = fees[0],fees[1],fees[2],fees[3]
    dic = {}
    for record in records:
        # 05:34 5961 IN
        time, number, state = record.split(" ")
        h,m = map(int,time.split(':'))

        
        # 딕셔너리에 있으면 추가 (입차)
        if not number in dic:
            dic[number] = [h*60+m,0,state]
            
#       출차
        if state == 'OUT':
            dic[number][1] = dic[number][1]+calculator(dic[number][0],h*60+m,basic_time,basic_fee,extra_time,extra_fee)
            dic[number][2] = 'OUT'
            continue
#       재입차
        if state == 'IN':
            dic[number][0] = h*60+m
            dic[number][2] = 'IN'
            continue
#     차량이 남아있을 경우 23:59분의 요금으로 계산
    for number in dic:
        if dic[number][2]=='IN':
            dic[number][1] = dic[number][1]+calculator(dic[number][0],23*60+59,basic_time,basic_fee,extra_time,extra_fee)
            dic[number][2] = 'OUT'
            
    result = []
    # dic.sort(ascending = True)
    dic = sorted(dic.items())
        
    for number in dic:
        # print(number)
        result.append(number[1][1])
        
    return result

