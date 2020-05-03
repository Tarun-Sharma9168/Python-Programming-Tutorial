'''
   Author name :     Tarun Sharma 
   Problem Statement: Finding the simple interest 
   
   
'''   
def simple_interest(p,t,r):
  return (p*r*t)/100

p=int(input("principal amount"))
r=int(input("rate of interest"))
t=int(input("time"))

result=simple_interest(p,r,t)
print('the simple interest calculated is {0}'.format(result))