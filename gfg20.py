'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: copying or cloning of the list

''' 

def cloning1(arr):
    #if we do with slicing 
    copy=arr[:]
    return copy

def cloning2(arr):
    copy=arr.copy()
    return copy

def cloning3(arr):
    copy=list(arr)
    return copy

def cloning4(arr):
    copy=[]
    copy.extend(arr)
    return copy

def cloning5(arr):
    copy=[i for i in arr]
    return copy
    
n=int(input('enter the size of the array'))
arr=[] 
for i in range(n):
    p=int(input('enter the element'))
    arr.append(p) 
#element=int(input('enter the element to search')) 
print(cloning1(arr))
print(cloning2(arr))
print(cloning3(arr))
print(cloning4(arr))
print(cloning5(arr))