'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: List the prime numbers in a given range

''' 

import math as mp
def prime_or_not(n):
    for i in range(2,int(mp.sqrt(n))):
        if(n % i == 0):
            return 0
    
    return 1
def prime_in_range(start,end):
    prime_list=[]    
    for i in range(start,end+1):
        if(prime_or_not(i)):
            prime_list.append(i)
    return prime_list

start=int(input("starting of the range\n"))
end=int(input("end of the range\n"))
print(prime_in_range(start,end))        
            
        
    