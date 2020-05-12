'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: count the number of words which are having the length greater than k

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
def find_words_length_greater_than_K(str1,k):
    list=str1.split(" ")
    count=0
    for i in list:
        if (len(i) > k):
            count=count+1
    
    return count        
#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp=input()
k=int(input())
#Calling of the functions that are there in the code section 
print(find_words_length_greater_than_K(inp,k))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)