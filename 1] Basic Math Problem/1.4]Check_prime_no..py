#Prime number:-
n=int(input("Enter the number:-"))
if n==0 or n==1:
    print("The given number is not the prime number")

else:
    for i in range(2,n):
        if n%i==0:
            print("The number is not the prime number")
            break
    else:
        print("The number is the prime number")