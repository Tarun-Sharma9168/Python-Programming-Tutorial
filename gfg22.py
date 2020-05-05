'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: 

''' 
#library Sections 

import sys
from time import perf_counter
sys.stdin =open('input.txt','r')
#sys.stdout=open('output.txt','w')


#main code here

def sum_of_all_elements_naive(arr):
    sum=0
    for i in arr:
        sum=sum+i     
    return sum
def sum_with_recursion(arr,size):
    if(size == 0):
        return 0
    else:
        return arr[size-1]+sum_with_recursion(arr,size-1)
        
def sum_with_sum_function(arr):
    return sum(arr)


#Input Output Starts from here 

t1_start=perf_counter()
n=int(input())
arr=list(map(int,input().split()))
#element=int(input('enter the element to search'))
print(sum_of_all_elements_naive(arr))
print(sum_with_recursion(arr,n))
print(sum_with_sum_function(arr))
 
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)