#Given an space seperated integer list find the average of elements present in the even index
my_list=list(map(int,input().split(" ")))
sum=0
count=0
n=len(my_list)
for i in range(len(my_list)):
    if(i%2==0):
     sum+=my_list[i]
     count+=1
print(sum/n)

#for average of all numbers if condition is not needed