import math
a=int(input())
r=a**0.5
c=0
if a<2:
    print("Not a prime number")
for i in range (2,int(r+1)):
    if(a%i==0):
        c+=1
        break
if c==0:
    print("Prime")
else:
    print("Not Prime")