'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Python program to find uncommon words from two Strings

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
def find_uncommon_words(a,b):
    new_list=[]
    
    #try to make hashing table of all the words = []
    a=a.split(" ")
    b=b.split(" ")

    dict={}
    for i in a:
        dict[i]=dict.get(i,0)+1
        
        
    for i in b:
        dict[i]=dict.get(i,0)+1
        
   # for i in dict.items():
   #     if(i[1] == 1):
   #         new_list.append(i[0])
    for i in dict.keys():
        if(dict[i] == 1):
            new_list.append(i)
                
                    
    return new_list
    
def uncommon_words_part2(a,b):
    new_list=[]
    for i in a.split(" "):
        if i not in b.split(" "):
            new_list.append(i)
            
    for i in b.split(" "):
        if i not in a.split(" "):
            new_list.append(i)        
            
    return new_list        
            
    

#Driver code 


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp1=input()
inp2=input()
#Calling of the functions that are there in the code section 
print(find_uncommon_words(inp1,inp2))
print(uncommon_words_part2(inp1,inp2))
t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)