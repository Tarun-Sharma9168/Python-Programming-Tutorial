'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: check if the string is palindrome or not

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


def do_reverse(str):
    reverse_copy=str[::-1]
    return reverse_copy

def is_palindrome(str):
    if(do_reverse(str) == str):
        return True
    else:
        return False 
    
def another_way(str):
    new_str=''.join(reversed(str))
    if(str == new_str):
        return True
    else:
        return False
    

#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
s=input()
#Calling of the functions that are there in the code section 
if(is_palindrome(s)):
    print("string is palindrome")
else:
    print("string is not palindrome")

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)