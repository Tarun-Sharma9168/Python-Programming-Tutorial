'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Checking of the Number is Armstrong or not

'''   
#Function calculating the Power
def power(x,n):
    if(x > 0 and n==0):
        return 1
    if(x == 0 ):
        return 0;
    if(n % 2 ==0):
        result=power(x,n/2)*power(x,n/2)
        return result
    if(n%2 ==1):
        result=x*power(x,n-1);
        return result        
#Function calculating the Power
def order(n):
    count=0
    while(n > 0):
        count=count+1;
        n=n//10
    return count    

#Function checking the number is Armstrong or not
def Armstrong_or_not(x):
    temp=x
    n=order(x)
    sum=0
    while(x):
        p=x%10
        sum=sum+power(p,n)
        x=x//10
    if(sum == temp  ):
        return 'yes...'
    else:
        return 'nope...'    
print(Armstrong_or_not(1253)) 
print(Armstrong_or_not(153))   
        