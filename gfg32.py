'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Break a list into n sized chunk lists using yield keyword which has amazing usage...
   The yield keyword enables a function to comeback where it left off when it is called again. This 
   is the critical difference from a regular function. A 
   regular function cannot comes back where it left off. The yield keyword helps a function to remember its state. 
   The yield enables a function to suspend and resume while it turns in a value at the time of the suspension of the execution.
    
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
def divide_chunks(l,n):
    for i in range(0,len(l),n):
        yield l[i:i+n]

def divide_chunks2(l,n):
    x=[l[i:i+n] for i in range(0,len(l),n)]
    return x
        


#Input Output Section
t1_start=perf_counter()
n=int(input())
arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 

x=divide_chunks(['geeks', 'for', 'geeks', 'like', 'geeky','nerdy', 'geek', 'love', 'questions','words', 'life'],5)
print(list(x))

x=divide_chunks2([1, 2, 3, 4, 5, 6, 7, 8, 9] ,3)
print(x)
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)