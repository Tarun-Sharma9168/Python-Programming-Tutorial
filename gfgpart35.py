'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: removing the key from the dictionary we can do this by using pop,del and the dict comprehension...

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


#Driver code 


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 

#Calling of the functions that are there in the code section 
# Python code to demonstrate 
# removal of dict. pair 
# using items() + dict comprehension 

# Initializing dictionary 
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21} 

# Printing dictionary before removal 
print ("The dictionary before performing remove is : " + str(test_dict)) 

# Using items() + dict comprehension to remove a dict. pair 
# removes Mani 
new_dict = {key:val for key, val in test_dict.items() if key != 'Mani'} 

# Printing dictionary after removal 
print ("The dictionary after remove is : " + str(new_dict)) 


t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)