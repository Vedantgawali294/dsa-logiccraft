#sum of even number from 1 to n:-
n=int(input("Enter the number:-"))
i=2
sum=0
while i<=n:
    sum=sum+i
    i=i+2
    print(sum)


#in for loop:-
n=int(input("Enter the number:-"))
sum=0
for i in range(2,n+1,2):
    sum=sum+i
    print(sum)
    
