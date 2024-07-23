#find the element that is present in K+N index.
my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
if(len(my_list)<k+n):
    print("ERROR")
else:
     for i in range(0,len(my_list)):
          print(my_list[k+n],end=" ")
          break