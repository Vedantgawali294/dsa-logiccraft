#Reverse number from n to 1:-
#in while loop :-
n=int(input("Enter the number:-"))
i=n
while i>=1:
    print(i)
    i=i-1


#in for loop :-
n=int(input("Enter the number:-"))
i=n
for i in range(n,0,-1):
    print(i)