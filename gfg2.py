'''
   Author name :     Tarun Sharma 
   Problem Statement:Factorial of a number
   
   
'''   
def fact(n):
    return 1 if n==0 or n==1 else n*fact(n-1)
n=input("enter the number") 
result=fact(int(n))
print('the factorial of a {0} is {1}'.format(n,result))