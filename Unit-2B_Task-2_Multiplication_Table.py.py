n=int(input("Enter the number:"))
for n in range(n,n*11,n):
    print(f"{n}")

n = int(input("Enter the number:" ))
count = 0 
while count<=10:
    print(f"{n} x {count} = {n*count}")
    count+=1