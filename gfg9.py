'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Rotation but now one by one see carefully the code....

''' 
def left_rotate(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp    
    return arr    
def rotate(arr,d,n):
    for i in range(d):
        left_rotate(arr,n)
    return arr 
n=int(input('enter the size of array'))
d=int(input('the number of places to rotate'))
new_list=[]
for i in range(n):
    p=int(input('enter the number'))
    new_list.append(p)
print(rotate(new_list,d,n))    
             