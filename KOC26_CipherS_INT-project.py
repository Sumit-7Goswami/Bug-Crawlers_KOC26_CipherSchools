##Project-->19

# ---- Your task is to write a program to find n'th  prime palindrome number , n is the input user will five.



n=int(input("Enter a  number: "))     
rev = int(str(n)[::-1])
if n == rev:
    if n>1:
        for i in range (2,n):
            if (n%i)==0 :
                print(n , "is not a prime! but it is palindrome")
            else:
                print(n, "is a prime as well as palindrome")
                break
else:
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                print(n,"is not prime number! as well as it is not palindrome")
                break
        else:
            print(n,"is prime number but not palindrome")



