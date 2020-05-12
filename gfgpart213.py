'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: remove the ith character from the string using slicing and the string replace 
                      str.replace(to_replace ,from what)

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
def remove_ith_character(str,i):
    a=str[:i]
    b=str[i+1:]
    
    return a+b
def using_replace_function(str,i):
    for j in range(len(str)):
        if j==i:
            str=str.replace(str[i],'')
    return str       
#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp=input()
i=int(input())
#Calling of the functions that are there in the code section 
print(remove_ith_character(inp,i))
print(using_replace_function(inp,i))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)