import math

def get_total_minutes(date):
    h, m = map(int, date.split(':'))
    return h*60 + m
    
def solution(fees, records):
    answer = []

    dtime, dfee, atime, afee = fees  
    log_dict = {}
    car_list = []
    for each in records:
        time, car_num, inout = each.split()
        
        if log_dict.get(car_num):
            log_dict[car_num].append([get_total_minutes(time), inout])
        else:
            log_dict[car_num] = [[get_total_minutes(time), inout]]
            car_list.append(car_num)
    
    car_list.sort()
    
    for car_num in car_list:
        ttime = 0
        
        log_list = log_dict[car_num]
        if log_list[-1][-1] == "IN":
            log_list.append([get_total_minutes('23:59'), "OUT"])
        
        for log in log_list:
            log_time, log_type = log
            if log_type == "OUT":
                ttime += log_time
            else:
                ttime -= log_time
        
        if ttime <= dtime:
            answer.append(dfee)
        else:
            tfee = dfee + math.ceil((ttime-dtime) / atime) * afee
            answer.append(tfee)        

    return answer