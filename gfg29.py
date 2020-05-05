'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Remove empty tuples if any are there in the list....
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

#using list comprehension
def func1(arr):
    arr=[ele for ele in arr if ele]
    return arr


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
tuples= [(), ('ram','15','8'), (), ('laxman', 'sita'),  
          ('krishna', 'akbar', '45'), ('',''),()] 
#Calling of the functions that are there in the code section 
print(func1(tuples))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)