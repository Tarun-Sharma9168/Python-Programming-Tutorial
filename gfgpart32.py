'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Handling missing values in python basically in dictionary which can be cause generally...
   collections has a function defaultdict

'''

#library section 
import collections
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


#Driver code 


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

arr=collections.defaultdict(lambda: 'key not found')
arr['a']=1
arr['b']=2


print(arr['a'])

print(arr['b'])
print(arr['c'])
#Calling of the functions that are there in the code section 


t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)