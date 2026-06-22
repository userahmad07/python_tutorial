import math # Importing the math module to use mathematical functions
course = "Python Programming"
course1 = "Python \nProgramming" # \n is used to create a new line
print (course)
print (course1)

FName = "Ahmad"
LName = "Ashfaq"
Full = FName + " " + LName # Concatenation of strings the " " is used to add a space
print (Full)
Full1 = f"{FName} {LName}" # f-string formatting this is a more modern way to format strings
print (len(Full1)) # len() is used to find the length of a string

print(course.lower())   # lower() is used to convert a string to lowercase. There are also upper() and title() methods

print(course.find("hon Programming")) # find() is used to find the index of a substring in a string. If the substring is not found, it returns -1

print(course)


print(course.replace("P", "A"))

print("pro" in course) # in is used to check if a substring is present in a string. It returns True or False
print("java" not in course) # not in is used to check if a substring is not present in a string. It returns True or False



print(10 + 5) # Addition
print(10 - 5) # Subtraction
print(10 * 5) # Multiplication
print(10 / 5) # Division
print(10 // 5) # Floor Division (Returns the value without the decimal part)
print(10 ** 5) # Exponentiation (10 raised to the power of 5)


print(round(1.4)) # round() is used to round a number to the nearest integer

x = 10.12
print(round(x))


print(abs(-99)) # abs() is used to get the absolute value of a number, Basically, it removes the negative sign if present

print(math.degrees(2.15)) # math is a module that provides access to mathematical functions. degrees() converts radians to degrees and there are many other functions available, But we have to import the math module.

#TYPE CONVERSION
x = input ("x: ")
y = 1

print(y + int(x)) # Here int is Converting x to integer before performing addition. this is called type conversion.

#BOOLEAN
# The number 0, Empty String "", and the term "None",and "False" are considered False in Python. Everything else is considered True.

#Comparison Operators
10 > 5 # Greater than, here > is a comparison operator.

Temperature = 42

if Temperature == 41:
    print("It's if")

elif Temperature > 30:
    print("It's elif")

else:
    print("It's else")


age = 12

if age <= 18:

    message = "You are a minor"
else:
    message = "You are an adult"

print(message)

age = input("x:")

print("Congrats") if age >= str("18") else "You are a minor" # This is a conditional expression (also known as a ternary operator). A ternary operator is a shorthand way of writing an if-else statement. It evaluates the condition before the `if` and returns the value after the `if` if the condition is true, or the value after the `else` if the condition is false.

# and, or, not Operators

highly_educated = True
skilled = False
talented = True

if highly_educated and skilled:
    print("You are educated and skilled")
elif skilled and talented and not highly_educated:
    print("You are good")
elif not skilled or talented:
    print("You are useless talent")


man_age = 66

if 18<= man_age <65: # This is a chained comparison, which checks if the value of `man_age` is between 18 and 65 (inclusive of 18 and exclusive of 65).
    print("You are an adult")
else:
    print("You are not an adult")

for ahmad in range(4): #Here range(4) generates a sequence of numbers from 0 to 3 (4 is not included). and the ahmad variable takes each value in that sequence one by one.
    print("For loop")
    print("Atempt", (ahmad +1), (ahmad + 1) * (".")) # Here when we write (ahmad + 1) * ("."), it repeats the string "." (dot) (ahmad + 1) times. For example, if ahmad is 0, it will print "." once, if ahmad is 1, it will print "." twice, and so on.
  
for ahmad in range(1, 12, 3): # Here range(1, 12, 3) generates a sequence of numbers starting from 1 to 11 (12 is not included) with a step of 3. So it will generate the numbers 1, 4, 7, and 10.
    print("Atempt", (ahmad), (ahmad) * ("."))

#Now If you want to hop out of the loop at some stage, you can use the break statement.

Result = False
for ahmad in range(3):
    if Result:
        print("Congrats!")
        break
else:
    print("Tried 3 times, but no result found.") # The else block after the for loop will execute only if the loop completes without hitting a break statement.


for hassan in range(3):
    for tariq in range(2):
        print(hassan, tariq)


def addition(x, y):
    return x + y

print(addition(23, 42))

print ("Program Successful")