'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Remove the ith character from the string....
                      There are nearly four methods....

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
def remove_ith_first(s,index):#index to remove
    str=""
    for i in range(len(s)):
        if(i!=index):
            str=str+s[i]
    return str 
def remove_ith_second(s,index):
    main_ans=s[:index]+s[index+1:]
    return main_ans

#using the str.replace function 
#two way one replace method replaces all the occurences and second one first occurence of some element x
def remove_ith_third(s,index):
    new_str=s.replace('e','')#as s.replace() wont work because string is immutable
    #second way
    new_str2=s.replace('s','',1)#removing the first occurence
    return new_str,new_str2

#you can use list comprehension also but it is same as first one ...    
    


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
s=input()
n=int(input())

#Calling of the functions that are there in the code section 
print(remove_ith_first(s,n))
print(remove_ith_second(s,n))
print(remove_ith_third(s,n))


t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)