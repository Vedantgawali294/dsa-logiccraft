#Reverse a given number:-
n=int(input("Enter the number:-"))
i=n
while i>0:
    print(i%10,end="")
    i=i//10