'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: sorting the dictionary using the different function

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
def sort_using_key(arr):
    for i in sorted(arr.items()):
        print(i,end=' ')
    print()    
        
def sort_using_value(arr):
    arr=sorted(arr.items() ,key=lambda kv:(kv[1],kv[0]))
    return arr         


#Driver code 


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 


arr={'a':1,'b':4,'z':32,'t':44,'e':12}

#Calling of the functions that are there in the code section 
print(sort_using_value(arr))
sort_using_key(arr)
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)