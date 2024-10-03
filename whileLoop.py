#while loop = used to repeat a block of code as long as a condition remains True
#             we re-check the condition at the end of the loop

name = input("Enter your name: ")
while name == "":
    name = input("Enter your name: ")

print(f"Hello {name}")    
