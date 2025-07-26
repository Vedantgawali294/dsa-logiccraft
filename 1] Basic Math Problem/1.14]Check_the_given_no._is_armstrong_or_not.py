#Check whether the given number is armstrong or not
n=int(input("Enter the number:-"))
i=n
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
    if sum==n:
        print("The given number is armstrong")
        break
else:
    print("The given number is not armstrong")