'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: count number of vowels using set data structure
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
sys.stdout=open('output.txt','w')
#Code Section
def vowel_count(str):
    vowel_list=[]
    for i in str:
        if i in "aeiouAEIOU":
            vowel_list.append(i)
    
    return len(vowel_list)       

#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp=input()
#Calling of the functions that are there in the code section 
print(vowel_count(inp))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)