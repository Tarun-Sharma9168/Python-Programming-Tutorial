'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Program to print the duplictes in the list....using set DataStructure using some extra space but time efficient...

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

def print_duplicates(arr):
    already_in=set()
    duplicates=set()
    for i in arr:
        if i in already_in:
            duplicates.add(i)
        else:
            already_in.add(i)
    return duplicates        
                
        
#Input Output Section
t1_start=perf_counter()
n=int(input())
arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 
print(print_duplicates(arr))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)