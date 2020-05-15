'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: sum of all items in a dictionary

'''

#library section 
from collections import Counter
import sys
import numpy as np
from functools import reduce
from time import perf_counter
import math
import re
sys.stdin =open('input.txt','r')
#sys.stdout=open('output.txt','w')
#Code Section
def sum_of_all_terms(arr):
    sum=0
    for i in arr.items():
        sum=sum+i[1]
    return sum    
        
def second_approach(arr):
    sum=0
    for i in arr.values():
        sum=sum+i
        
    return sum    
#Driver code 


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", sum_of_all_terms(dict)) 
print("Sum :",second_approach(dict))
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)