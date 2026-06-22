# A module is nothing but a python file that can be imported inside another python file. Like we're goinf to do here by writing some functions and then calling them from the odules.py file.

#When you import a module in Python (like import faisalabad), all the top-level code in that module is executed immediately. This includes any print statements that are not inside a function or guarded by an if __name__ == "__main__": block

from random import choice


landmark = "Ghanta Ghar"

Speciality = "Jugtein"

Language = "Punjabi"


def shehar():
    "Faisalabad is good city of Pakistan."
    
    print(shehar.__doc__) #This prints the docstring of the function Faisalabad which is a brief description of the function. You can also access the docstring of a function by using the help() function like so: help(Faisalabad). A docstring is a string that describes a function, class or module. It is used to explain the purpose of the function, class or module.

def overview(): #How you wrote it earlier, Made a description of a function rather than providing a value to it. This is how you should provide a value. 
    city = [
        "Faisalabad is the 3rd largest city of Pakistan.",
        "It is known as the Manchester of Pakistan because of its textile industry.",
        "It is famous for its Ghanta Ghar, Jugtein and Punjabi Language and culture.",
        "Faisalabad is also known for its agriculture and is a major contributor to the country's economy from cloth and textile industry."
    ]

    indx = choice("0123") #This will simply select a number from 0 to 3, Nothing that makes it the index of the city list
    return(city[int(indx)]) # This is quite simple but confusing logic, This actually makes the random selected number the index of a list. Firstly the city[] this requires for a number (As the list has 4 items, We can add any number from 0 to 3 and that will be the index) But we want it random. SO rather than passing a specific number we pass a logic to firstly convert the randomly selected number to integer by int(indx) which basically means convert the value of indx to integar and that integer is passed as the index of the list.


if __name__ == "__main__":
    print("Hi, Boss! You are in main module.")

    