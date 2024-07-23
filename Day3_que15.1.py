#Find the unique in the array.
my_list=list(map(int,input().split(" ")))
new_list=[]
for i in my_list:
    if(i in new_list):
        new_list.append(i)
print(*new_list)