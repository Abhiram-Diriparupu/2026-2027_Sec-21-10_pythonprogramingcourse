def total_marks_of_the_student(mark1,mark2,mark3):
    return mark1+mark2+mark3
def average_marks_of_the_student(mark1,mark2,mark3):
    return (mark1+mark2+mark3)/3

mark1=int(input("enter the first subject marks:"))
mark2=int(input("enter the second subject marks:"))
mark3=int(input("enter the third subject marks:"))

print("total_marks=",total_marks_of_the_student(mark1,mark2,mark3))
print("average_marks=",average_marks_of_the_student(mark1,mark2,mark3))