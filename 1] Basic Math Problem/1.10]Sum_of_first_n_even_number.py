#Sum of first n even number:-
n=int(input("Enter the number:-"))
i=2
sum=0
count=0
while count<n:
    if i%2==0:
        sum=sum+i
        count=count+1

    i=i+1
print("Sum of first n even number is:-",sum)        