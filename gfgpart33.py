'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: python dictionary with keys having the multiple inputs 

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
import random as rn 
  
# creating an empty dictionary 
dict = {} 
  
# Insert first triplet in dictionary 
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z; 
  
# Insert second triplet in dictionary 
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z; 
  
# print the dictionary 
print(dict) 


places = {("19.07'53.2", "72.54'51.0"):"Mumbai",("28.33'34.1", "77.06'16.6"):"Delhi"}
print(places)
print("\n")


lat = [] 
long = [] 
plc = [] 
for i in places: 
    lat.append(i[0]) 
    long.append(i[1]) 
    plc.append(places[i[0], i[1]]) 
  
print(lat) 
print(long) 
print(plc)  

t1_end=perf_counter()
print('total elapsed time',t1_start-t1_end)