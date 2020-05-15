'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: left and right rotation through the array slicing and all

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
def rotate(input,d): 
  
    # slice string in two parts for left and right 
    Lfirst = input[0 : d] 
    Lsecond = input[d :] 
    Rfirst = input[0 : len(input)-d] 
    Rsecond = input[len(input)-d : ] 
  
    # now concatenate two parts together 
    print("Left Rotation : ", (Lsecond + Lfirst)) 
    print("Right Rotation : ", (Rsecond + Rfirst)) 

#Driver code 
def check_empty(s,sub_str):
    if(s == ''):
        return True
    index=s.find(sub_str)
    new_s=s[0:index]+s[index+1:]
    check_empty(new_s,sub_str)
    return False
    

#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
d=int(input())
inp=input()
#Calling of the functions that are there in the code section 
rotate(inp,d)

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)