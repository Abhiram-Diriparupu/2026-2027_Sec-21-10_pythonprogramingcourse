#finding compund interest 
principle=int(input("enter the principle:"))
Rate=int(input("enter the rate in percentage:"))
time=int(input("enter the time in years:"))
Amount=principle*(1+Rate/100)**time
compound_interest=Amount-principle
print(compound_interest)