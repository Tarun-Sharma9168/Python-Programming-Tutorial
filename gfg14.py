'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Reconstruct the array by replacing arr[i] with (arr[i-1]+1) % M
''' 
def reconstruct_the_array(arr,n,m):
    ind=0
    for i in range(n):
        if(arr[i]!=-1):
            ind=i
            break
    #calculating the values from ind-1 to 0
    for i in range(ind-1,-1,-1):
        if(arr[i]==-1):
            arr[i]=(arr[i+1]-1+m)%m
            
    # Calculating the values of the indexes ind + 1 to n 
    for i in range(ind + 1, n): 
        if(arr[i]==-1): 
            arr[i]=(arr[i-1]+1)% m
    
    return arr                     
       
print(reconstruct_the_array([5, -1, -1, 1, 2, 3],6,7))          