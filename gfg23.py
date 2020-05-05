'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: 

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
def prod1(arr):
    mul=1
    for i in arr:
        mul=mul*i
    return mul

def prod2(arr):
    return np.prod(arr)

def prod3(arr):
    return  reduce(lambda x,y : x * y , arr)

'''
def prod4(arr):
    return math.prod(arr)
    #available in python 3.8
'''       

#Input Output Section
t1_start=perf_counter()
n=int(input())
arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 
print(prod1(arr))
print(prod2(arr))
print(prod3(arr))
#print(prod4(arr))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)