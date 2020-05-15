'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: give the duplicates in the string

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
def count_duplicates(inp):
    WC=Counter(inp)
    j=-1
    for i in WC.items():
        a,b=i
        if(b > 1):
            print(a,end=' ') 
    print()           
        
        

#Driver code 


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp=input()
#Calling of the functions that are there in the code section 
count_duplicates(inp)

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)