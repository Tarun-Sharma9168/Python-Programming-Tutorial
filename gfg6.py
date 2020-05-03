'''      ######  
         #                       #####  
         #  ###  ### #####       #   
         #    #  ###   #         #####   #### ##### 
         ######  ###   #             #   ####   # 
                                 #####   ####   #
   Author name :      Tarun Sharma 
   Problem Statement: Checking of the Number is Fibonacci number or not

''' 
import math
def is_perfect_square(n):
    s=int(math.sqrt(n));
    return s*s == n
def is_fib_n(n):
    if(is_perfect_square(5*n*n + 4 ) or is_perfect_square(5*n*n - 4)):
        return True
    else:
        return False

n=int(input("enter the number to check\n"))
print(is_fib_n(n))            