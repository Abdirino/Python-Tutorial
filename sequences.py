# List [] = mutable, most flexible
# Tuple () = immutable, faster
# Set {} = mutable, (add/remove), unordered, No duplicates, best for membership testing

fruits = ["apple", "mango", "orange", "coconut"]

for fruit in fruits: 
    print(fruit, end=" ")

#fruits.append = adds element to the end
#fruits.remove = removes element to the end
#fruits.pop = adds element to the start