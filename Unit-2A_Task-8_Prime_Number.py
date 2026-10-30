#checking whether the given number is prime or not 
number = int(input("Enter the number between 1 to 100:"))
if number>100:
    print(f"{number} is not in the range of 1 to 100")
elif number<=1:
    print(f"{number} is  not a prime number")
elif number ==2:
    print(f"{number} is a prime number ")
elif number ==3:
    print(f"{number} is a prime number ")
elif number ==5:
    print(f"{number}is a prime number")
elif number ==7:
    print(f"{number} is a prime number")
elif number%2==0:
    print(f"{number} is not a prime number")
elif number%3==0:
    print(f"{number} is not a prime number ")
elif number%5==0:
    print(f"{number} is not a prime number ")
elif number%7==0:
    print(f"{number} is not a prime number ")
else:
    print(f"{number} is a prime number")