'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Reversal algorithm for rotating  the array

''' 
def reverse_array(left,right,arr):
    while(left < right):
        temp=arr[left]
        arr[left]=arr[right]
        arr[right]=temp
        left=left+1
        right=right-1
    return arr    
def rotate(arr,d,n):
    reverse_array(0,d-1,arr)
    reverse_array(d,n-1,arr)
    reverse_array(0,n-1,arr)
    
    return arr
print(rotate([1,2,3,4,5,6],2,6))