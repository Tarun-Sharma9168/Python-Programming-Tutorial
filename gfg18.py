'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: python ways to check if element exist in the list or not..
                      bisect_left function such as lower_bound() in c++ stl amazing..

''' 
from bisect import bisect_left
def naive_searching(arr,element): 
    for i in arr:
        if(i == element):
            return True
    return False    
    
def set_way(arr,element):
    pp=set(arr)
    if element in pp:
            return True
    return False
def second_way(arr,element):
    arr.sort()
    pp=(bisect_left(arr,element))
    if(pp == len(arr)):
        return False
    return True
    
n=int(input('enter the size of the array'))
arr=[] 
for i in range(n):
    p=int(input('enter the element'))
    arr.append(p) 
element=int(input('enter the element to search'))     
print(naive_searching(arr,element))  
print(set_way(arr,element))  
print(second_way(arr,element))
