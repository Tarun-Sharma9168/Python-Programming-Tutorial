'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Check if a substring is there in it or not .....

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
def check_substr(str_,sub_str):
    if(str_.find(sub_str)!=-1):
        return "YES"
    else:
        return "NO"
 
 
 #One alternative method is using the count method..
def using_count(str_,sub_str):
    if(str_.count(sub_str) > 0):
        return "YES"
    else:
        return "NO"
     
#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
str_=input()
sub_str=input()
#Calling of the functions that are there in the code section 
print(check_substr(str_,sub_str))
print(using_count(str_,sub_str))
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)