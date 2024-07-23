#reverse of a number
n=1234
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(int(rev))