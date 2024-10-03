#if statements = executes some code only if a condition is True
#                they allow the basics decision-making
#                (if, elif, else)

age = int(input("Enter your age: "))

if age >= 17:
    print("You are an adult")
elif age == 0: 
    print("just born")  
elif age >= 65:
    print("senior Citizen")
else: 
    print("You are a child")    