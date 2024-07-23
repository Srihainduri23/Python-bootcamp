a=int(input("Enter first Number:"))
b=int(input("Enter Second Number:"))
while b!=0:
    a,b=b,a%b
print("GCD of 2 numbers is:",a)