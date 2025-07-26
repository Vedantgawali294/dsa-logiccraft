#check the given number is palimdrome or not:-
n=int(input("Enter the number:-"))
i=n
rev=0
while i>0:
    rev=(rev*10)+(i%10)
    i=i//10
    if (n==rev):
        print("Number is palindrome")
else:
    print("Number is not palindrome")