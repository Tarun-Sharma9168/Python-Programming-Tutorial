'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: rotating the list using temporary array
''' 
def rotate(arr,d,n):
     temp=arr[0:d];
     arr=arr[d:n]
     
     arr=arr+temp;
     return arr
n=int(input('enter the size of array'))
d=int(input('the number of places to rotate'))
new_list=[]
for i in range(n):
    p=int(input('enter the number'))
    new_list.append(p)
print(rotate(new_list,d,n))    
     