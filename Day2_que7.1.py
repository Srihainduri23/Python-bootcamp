#you are given with comma seperated natural numbers 1 to 10.Print only the even numbers.
my_list=list(map(int,input().split(",")))
for i in range(1,len(my_list),2):
    print(my_list[i])
