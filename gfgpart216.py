'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: get all the close matchec string that are there in a given to the given 
                      string.good using of the difflib library

'''

#library section 
#using the difflib library 
#this library is basically used for sequence matching sentence ,document and files even
from difflib import get_close_matches
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
def get_close_match_func(new_list,str):
    return get_close_matches(str,new_list)

#Driver code 


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

inp=input()
inp_list=input().split()

#Calling of the functions that are there in the code section 
print(get_close_match_func(inp_list,inp))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)