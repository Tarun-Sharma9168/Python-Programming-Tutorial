'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Remove multiple elements from the list

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

#suppose deleting all odd elements
def func1(arr):
    for i in arr:
        if( i & 1):
            arr.remove(i)
    return arr       
#Remove adjacent elements from the list
def func2(arr):
    del arr[1:3]
    return arr

#Remove element using list comprehension
def func3(arr):
    unwanted={1,3}
    arr=[ele for ele in arr not in unwanted]
    return arr 
    

#Input Output Section
t1_start=perf_counter()
n=int(input())
arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 
print(func1(arr))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)