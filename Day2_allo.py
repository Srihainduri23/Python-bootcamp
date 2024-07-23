my_list=list(map(str,input().split(",")))
print(f"1.Append 2.Pop 3.Sort 4.Length")
print("Enter the choice")
choice=int(input())
if(choice==1):
    my_list.append(99)
    print(*my_list)
elif(choice==2):
    my_list.pop(2)
    print(*my_list)
elif(choice==3):
    my_list.sort()
    print(*my_list)
else:
    print(len(my_list))