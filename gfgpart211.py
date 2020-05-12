'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Generating random str1ings until a given str1ing is generated

'''

#library section 
from collections import Counter
import sys
import numpy as np
from functools import reduce
from time import perf_counter
import math
import re
import string
import random
import time
sys.stdin =open('input.txt','r')
#sys.stdout=open('output.txt','w')
#Code Section
def generate_random_str1ing(str1):

    possible_string=string.ascii_lowercase+string.digits+string.ascii_uppercase + '., !?;:'
        
        # To take input from user 
    # t = input(str1("Enter your target text: ")) 
    #make some random string of length of string given in the function
    attemptThis = ''.join(random.choice(possible_string) for i in range(len(str1))) 
    attemptNext = '' 
    
    completed = False
    iteration = 0
    
    # Iterate while completed is false 
    while completed == False: 
        print(attemptThis) 
        
        attemptNext = '' 
        completed = True
        
        # Fix the index if matches with  
        # the str1ings to be generated 
        for i in range(len(str1)): 
            if attemptThis[i] != str1[i]: 
                completed = False
                attemptNext += random.choice(possible_string) 
            else: 
                attemptNext += str1[i] 
                
        # increment the iteration  
        iteration += 1
        attemptThis = attemptNext 
        time.sleep(0.1) 
    
    # Driver Code 
    print("Target matched after " +str(iteration) + " iterations") 
    


#Input Output Section
t1_start=perf_counter()
#n=int(input())
#arr=list(map(int,input().split())) 
#element=int(input('enter the element to search')) 
inp=input()
#Calling of the functions that are there in the code section 
generate_random_str1ing(inp)

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)