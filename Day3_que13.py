#Replace the elements in the array with average of maximum and minimum element.
my_list=list(map(int,input().split(" ")))
maxi=my_list[0]
min=my_list[0]
for i in range(0,len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
for i in range(0,len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
avg=((maxi+min)/2)
for i in range(0,len(my_list)):
    my_list[i]=avg
print(*my_list)