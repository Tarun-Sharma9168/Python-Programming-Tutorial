'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: number of matching characters in a string...

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
def number_of_matching_characters(str1_,str2_):
    set1_=set(str1_)
    set2_=set(str2_)
    count=0
    for i in set1_:
        if i in set2_:
            count=count+1
    return count
       
       
def number_of_matching_characters_using_set_intersection(str1,str2):
    set1_=set(str1)
    set2_=set(str2)
    
    ans =set1_ & set2_  #that is using the set intersection is very important
    return len(ans)       
#it will count the repeated one also    
def using_re(str1,str2):
    c=0
    for i in str1:
       if  re.search(i,str2):
           c=c+1
    return c       
            
#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
str1=input()    
str2=input()
#Calling of the functions that are there in the code section 
print(number_of_matching_characters(str1,str2))
print(number_of_matching_characters_using_set_intersection(str1,str2))
print(using_re(str1,str2))
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)