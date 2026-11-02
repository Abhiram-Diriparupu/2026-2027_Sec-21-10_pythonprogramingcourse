n = int(input("Enter how many numbers:"))
largest = int(input("ENTER  A NUMBER:"))
for i in range(n-1):
    num = int(input("enter the number:"))
    if num > largest :
        largest = num 
    print(f"{largest} is the largest")