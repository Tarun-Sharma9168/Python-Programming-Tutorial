'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Reversed the string having more than one word and in actual donot reversed the words but in actual reverse the sentence..

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
def reverse_words_in_string(str):
    list_of_word=str.split()
    ans=' '.join(reversed(list_of_word))
    return ans
    
#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
s=input()
#Calling of the functions that are there in the code section 
print(reverse_words_in_string(s))

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)