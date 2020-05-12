'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: check if a string is binary or not using simple iteration or using set both are valid option
                      but optimized...

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
def check_if_binary_or_not(str):
    a=set(str)
    b={'0','1'}
    
    if(a==b or a=={'0'} or a=={'1'}):
        return True
    else:
        return False

#Driver code 

#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp=input()
#Calling of the functions that are there in the code section 
if(check_if_binary_or_not(inp)):
    print("String is binary")
else:
    print("String is not binary")
        
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)