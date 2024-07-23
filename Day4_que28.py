#To print LeapYear.
n=int(input("Enter the year:"))
if(n%400==0 or (n%4==0) or (n%10==0)):
    print("leap year")
else:
    print("not a leap year")