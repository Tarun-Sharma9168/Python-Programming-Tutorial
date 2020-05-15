'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: check if the string becomes empty if we regularly removes sub_str...

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
def check_empty(s,sub_str):
    if(s==''):
        return True
    if(s == '' and sub_str==''):
        return True
    if(sub_str ==''):
        return False
    
    index=s.find(sub_str)
    if(index == -1):
        return False
    
    new_s=s[0:index]+s[index+len(sub_str):]
    #print(new_s)
    return check_empty(new_s,sub_str)
    


#Driver code 


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
str_inp=input()
sub_str=input()
#Calling of the functions that are there in the code section 
if(check_empty(str_inp, sub_str)):
    print("String is empty now")
else:
    print("We are unable to make the string empty recursively")    

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)