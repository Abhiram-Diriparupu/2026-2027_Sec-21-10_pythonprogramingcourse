#sum and average of N numbers
input_numbers = int(input("Enter how many numbers:"))
total_sum = 0 
for input_index in range(input_numbers):
    entered_number = float(input("enter the number:"))
    total_sum = total_sum + entered_number
average = total_sum/input_numbers
print(f"sum = {total_sum}")
print(f"average = {average}")