#PYTHON LOGICAL OPERATORS EXERCISE
a=3
result = a>5 and a<10 #logical and operator
print("result of",a,"> 5 and",a,"<10:", result)
result = a>2 and a<10 #logical and operator 
print("result of",a,"> 2 and" ,a,"<10:", result)
result=a>5 or a<10 #logical or operator
print("result of",a,"> 5 or",a,"<10:", result)
result=a>5 or a<1
print("result of",a,"> 5 or",a,"<1:",result)
result=not(a>5)
print("result of",a,"not(a>5)":,result)