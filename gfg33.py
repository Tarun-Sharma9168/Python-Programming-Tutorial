'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Sort the first list using the second list

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
#Very nice approach interesting.....
def func1(list1,list2):
    new_list=zip(list2,list1)
    z=[x for _ , x in sorted(new_list)]
    return z
    
#Input Output Section
t1_start=perf_counter()
n=int(input())
arr2=list(input().split())
arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 
x=list(func1(arr2,arr))
print(x)
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)