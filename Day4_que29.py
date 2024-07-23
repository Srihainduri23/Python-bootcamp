#To print LeapYear.
n=int(input())
for i in range(2000,2025):
    if(n%400==0 or (n%4==0) or (n%10==0)):
      print(i)                                     
      #peek gcb password