'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Program to accept the strings which contains all vowels

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
def returns_strings_with_all_vowels(str_):
    set_of_vowels={'a','e','i','o','u'}
    str_=str_.lower()
    for i in str_:
        if i in set_of_vowels:
            set_of_vowels.remove(i)
    if(len(set_of_vowels) == 0):
        return "YES"
    else:
        return "NO"        
    
#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
str_=input()
#Calling of the functions that are there in the code section 
print(returns_strings_with_all_vowels(str_))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)