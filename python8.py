integer=int(input("enter a integer"))
if(integer%2!=0):
    print("weird")
elif(integer%2==0 and 2<=integer<=5):
    print("not weird")
elif(integer%2==0 and 6<=integer<=20):
    print("weird")
else:
    print("not weird")