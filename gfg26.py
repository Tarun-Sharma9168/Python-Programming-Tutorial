'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Finding the N largest elements

'''

#library section 
from collections import Counter
import sys
import numpy as np
from functools import reduce
from time import perf_counter
import math
sys.stdin =open('input.txt','r')
sys.stdout=open('output.txt','w')
#Code Section
def first_way_n_largest_element(arr,n):
    arr=set(arr)
    arr=list(arr)
    arr_of_max=[]
    
    while(n):
     max=arr[0]
     i=1
     while(i<len(arr)):
        if(arr[i] >  max):
            max=arr[i]
        i=i+1
     arr.remove(max)
     arr_of_max.append(max)
     n=n-1 
           
    return arr_of_max       

def second_way_n_largest_element(arr,n):
    arr.sort()
    return arr[-n:]#it means leave first n 

#Input Output Section
t1_start=perf_counter()
n=int(input())
arr=list(map(int,input().split())) 
n_largest=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 
print(first_way_n_largest_element(arr,n_largest))
print(second_way_n_largest_element(arr,n_largest))
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)