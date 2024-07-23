#find the sum of squares of digit in given number
n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r**2 #IMP
    n=n//10
print(sum)