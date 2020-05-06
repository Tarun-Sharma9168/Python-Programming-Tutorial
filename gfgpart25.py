'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: print the even length string words

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

def return_even_length_words(str_):
  new_list=[]
  a=str_.split()
  for i in a:
      if(len(i) %2 == 0):
          new_list.append(i)
  return new_list        
    
#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split()))     
#element=int(input('enter the element to search')) 
str_=input()
#Calling of the functions that are there in the code section 
print(return_even_length_words(str_))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)