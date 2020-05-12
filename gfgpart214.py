'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: split and join the string

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

def split(str):
    new_list=str.split(" ")
    return new_list
				
def join_the_string(new_list):
    return "-".join(new_list)			

#Driver code 
#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp=input()
#Calling of the functions that are there in the code section 
new_list=split(inp)
print(join_the_string(new_list))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)