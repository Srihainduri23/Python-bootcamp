#Password verifier.  MR.X is trying to create a new password for his instagram account these are the required conditions for creating a new password 
#condition 1:Minimum length is 8 and maximum length is 15
#condition 2:only @,/ is allowed in a password 
#condition 3: no spaces are allowed 
#condition 4:only alpha numerics are allowed
#you are supposed to print weak if length is exact 8 , medium 8-12,strong if length is between 12-15

a=" "
len=len(a)
if(len<8):
    print("Please follow the conditions")
for i in a:
    if(i in str[0] or str[1]):
        count+=1
    break
if():
elif(len==8):
    print("weak")
elif(7<len<13):
    print("Medium")
elif(12<len<16):
    print("Strong")