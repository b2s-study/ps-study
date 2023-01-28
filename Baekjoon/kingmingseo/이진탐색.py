import math
def BinarySearch(target, list):
    start = 0
    end = len(list)-1

    while (True):
        mid = math.ceil((start + end) / 2)

        if (start > end):
            print("찾는 값이 없습니다")
            break
        elif target > list[mid] :
            start = mid +1

        elif target < list[mid] :
            end = mid -1

        else :
            print(mid,"위치에 데이터가 있습니다")
            break


BinarySearch(66 ,[5, 8, 10 ,15 , 20, 25 , 30 , 40,50,54,66,69,83,86,90])