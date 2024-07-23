#Print the element in a particular index in cyclic printing.IMP
my_list=list(map(int,input().split(" ")))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])