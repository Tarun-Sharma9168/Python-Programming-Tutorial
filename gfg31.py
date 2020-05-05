'''
         ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Cumulative sum of an array using list comprehension.....
   
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
def Cumulative(lists):  
    cu_list = []  
    length = len(lists)  
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]  
    return cu_list[1:] 
  


#Input Output Section
t1_start=perf_counter()
n=int(input())
arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 
print(Cumulative([10, 20, 30, 40, 50]))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)