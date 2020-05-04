'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: check if the array is monotonic or not..that is either the array elements are either increasing or decreasing...
   

'''
def is_monotonic(A):
     return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
     
n=int(input('enter the size of the array'))
new_list=[]
for i in range(n):
    p=int(input('enter the number'))
    new_list.append(p)
print(is_monotonic(new_list))    
    
    