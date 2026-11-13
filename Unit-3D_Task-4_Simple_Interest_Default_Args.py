def simple_interest(principle,time,rate=5):
    return (principle*time*rate)/100
principle = int(input("enter the principle:"))
time = int(input("enter the time in years:"))

print("simple interest =",simple_interest(principle,time))
print("simple interest=",simple_interest(principle,time,rate=7))