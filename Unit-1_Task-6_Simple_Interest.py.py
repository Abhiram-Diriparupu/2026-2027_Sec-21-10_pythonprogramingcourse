#CALCULATING SIMPLE INTEREST
principle=int(input("enter the principle:") )
rate = int(input("enter the rate in percentage:"))
time = int(input("enter the time in years:"))
interest = principle*time*rate/100
print(interest)