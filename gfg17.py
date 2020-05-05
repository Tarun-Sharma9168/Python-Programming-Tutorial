'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: finding the ways to find the length of the list


'''
#len function is faster than the another new one that is length_hint()
from operator import length_hint
def first_way(arr):
    counter=0
    for i in arr:
        counter=counter+1
        
    return counter
def second_way(arr):
    return len(arr)

def third_way(arr):
    return length_hint(arr)

n=int(input('enter the length of array\n'))
arr=[]
for i in range(n):
    p=int(input('enter the element\n'))
    arr.append(p)
    
print(first_way(arr))
print('\n')
print(second_way(arr))
print('\n')
print(third_way(arr))    
        
    