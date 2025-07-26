#sum of product of digit of given number:-
n=int(input("Enter the number:-"))
i=n
sum=1
while i>0:
    sum=sum*(i%10)
    i=i//10
print(sum)    