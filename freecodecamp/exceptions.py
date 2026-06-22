#An exception is an error. There are some built in exceptions in python like ZeroDivisionError, FileNotFoundError, IndexError, KeyError, TypeError, ValueError etc. You can also create your own exceptions.
x = 6

try:
    if not type(x) is str: 
        raise TypeError("Only strings are allowed")
except NameError: #This will be raised if there is a NameError exception. A nameerror exception is built in exception.
    print("NameError means the variable is not defined")
except ZeroDivisionError: #This will be raised if there is a ZeroDivisionError exception. A ZeroDivisionError exception is built in exception.
   print("You can't divide a number by zero")
except Exception as error:
    print(error) #The output will be "division by zero" because the error variable will contain the error message.
else:
    print("No error occurred") #After the try block if there is no error this block will be executed.
finally:
    print("The error is printed")