#sum of even number & product of odd number:-
n=int(input("Enter the number:-"))
i=n
sum=0
prod=1
digit=0
while i>0:
    digit=i%10
    i=i//10
    if (digit%2)==0:
        sum=sum+digit
    else:
        prod=prod*digit

print("Sum of even number is:-",sum)
print("prod of even number is:-",prod)