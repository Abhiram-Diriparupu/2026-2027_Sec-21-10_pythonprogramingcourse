def area(length,breadth):
    return length*breadth
def perimeter(length,breadth):
    return 2*(length+breadth)

length = int(input("enter the length:"))
breadth = int(input("enter the breadth:"))

print("Area=",area(length , breadth))
print("Perimeter=",perimeter(length , breadth))