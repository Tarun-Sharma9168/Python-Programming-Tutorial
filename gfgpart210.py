'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: 

'''

#library section 
import re #regular expressin library
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
def remove_special_character(str):
   
   regex=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
   
   if(regex.search(str)==None):
       return 1
   else:
       return 0

#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp=input()
#Calling of the functions that are there in the code section 
if(remove_special_character(inp)):
    print("string accepted")
else:
    print("string rejected")

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)