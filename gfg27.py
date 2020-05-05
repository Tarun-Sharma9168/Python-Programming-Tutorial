'''     
         ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: print the even numbers in the list and also the odd

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
def odd_and_even(arr):
    arr_odd=[]
    arr_even=[]
    for i in arr:
        if(i & 1):
            arr_odd.append(i)
        else:
            arr_even.append(i)
        
    return arr_even,arr_odd   

def odd_and_even2(arr):
    even_nos = list(filter(lambda x: (x % 2 == 0), arr))
    odd_nos  = list(filter(lambda x: (x % 2 != 0),arr)) 
    
    return even_nos,odd_nos

def odd_and_even3(arr):
    even_nos=[i for i in arr if i%2==0]
    odd_nos =[i for i in arr if i%2!=0]
    
    return even_nos,odd_nos 
#Input Output Section
t1_start=perf_counter()
n=int(input())
arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 
print(odd_and_even(arr))
print(odd_and_even2(arr))
print(odd_and_even3(arr))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)