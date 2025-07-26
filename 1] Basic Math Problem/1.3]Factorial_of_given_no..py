#Factorial number:-
n=int(input("Enter the number:-"))
fact=1
if n==1 or n==0:
    print(1)

i=1
while i<=n:
    fact=fact*i
    i=i+1

print(fact)    