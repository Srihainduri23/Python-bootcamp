#find the sum of number 
# n=123 o/p=1+2+3=6.IMP

n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r #IMP
    n=n//10
print(sum)