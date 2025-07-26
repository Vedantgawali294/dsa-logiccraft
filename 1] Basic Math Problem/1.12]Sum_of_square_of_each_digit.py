#Sum of square of each digit:-
n=int(input("Enter the number:-"))
i=n
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)
    i=i//10

print(sum)    