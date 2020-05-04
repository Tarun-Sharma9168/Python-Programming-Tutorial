'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: A very nice theorm that is juggling thoerm to rotate the array good with the use of gcd

''' 
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
def rotate(arr, d, n): 
    for i in range(gcd(d,n)): 
          
        # move i-th values of blocks  
        temp = arr[i] 
        j = i 
        while 1: 
            k = j + d 
            if k >= n: 
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k] 
            j = k 
        arr[j] = temp 
    return arr   
n=int(input('enter the size of array'))
d=int(input('the number of places to rotate'))
new_list=[]
for i in range(n):
    p=int(input('enter the number'))
    new_list.append(p)
print(rotate(new_list,d,n))                 
        