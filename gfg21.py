'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Count the occurence of the element x. 

''' 
import sys
# For getting input
sys.stdin = open('input.txt', 'r')
from collections import Counter
def countx(arr,x):
    return arr.count(x)
def countx_naive(arr,x):
    count=0
    for i in arr:
        if(i == x):
            count=count+1 
    return count
def countx_usingCollection(arr,x):
    element_wise_dictionary=Counter(arr)
    return element_wise_dictionary[x]        

n=int(input())
arr=list(map(int,input().split()))
element=int(input())    
print('{} has occured {} times'.format(element,countx(arr,element)))
print('{} has occured {} times'.format(element,countx_naive(arr,element)))
print('{} has occured {} times'.format(element,countx_usingCollection(arr,element)))



