'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement:Largest element in an array

''' 
def Largest_element(arr):
    max_ele=arr[0]
    for i in range(1,len(arr)):
        if(arr[i]) > max_ele:
            max_ele=arr[i]            
    return max_ele 

n=int(input("size of the array\n"))
arr=[]
for i in range(n):
    p=int(input('enter the number\n'))
    arr.append(p)
print(Largest_element(arr))