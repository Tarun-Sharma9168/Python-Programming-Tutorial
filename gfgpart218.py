'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Program to swap comma and dots using maketrans
                      first one has some ambiguity because first two strings of maketrans function should have 
                      equal length..
                      Second function is preferable here...

'''

#library section 
import string
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
def translate_comma_and_dots(inp):
    final=inp.translate(inp.maketrans(', .' , '. ,'))
    return final     


def replace_comma_and_dots_part2(inp):
    inp=inp.replace(', ','third')
    inp=inp.replace('.',', ')
    inp=inp.replace('third','.')
    return inp
    
#Driver code 


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp=input()
#Calling of the functions that are there in the code section 
print(translate_comma_and_dots(inp))
inp=input()
print(replace_comma_and_dots_part2(inp))
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)