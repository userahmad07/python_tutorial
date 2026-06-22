#Here you'll learn about R A W X which stands for Read, Append, Write and Create.
import os  #
#Read
o = open("names.txt") #This will open and read the file.txt file.
#print(o.read())

#Now If you don't want to read the whole file
#print(o.read(6)) #This will only read the first 6 charchters
#print(o.readline()) #This will read the first line of the file. and if you just copy the same line again it will read the next line.
#print(o.readline()) #This will read the second line of the file.
#print(o.readlines()) #This will read all the lines and put them in a list. But in a list format. while others will read in string format.

for line in o :
    print(line)


o.close() #This will close the file. Always remember to close the file because it will free up the resources.

try:
    f = open("names.txt")
    print(f.read())
except:
    print("Sorry the file does not exist")
finally:
    f.close() #This will cause an error if the file does not exist.

#Append
a = open("names.txt", "a") #This will open the file in append mode
a.write("\nHusain") #This will add the name Husain at the end of the file.
a.close()

a = open("names.txt")
print(a.read())
a.close()

#Write (Overwrites)
w = open("names.txt", "w") #This will open the file in write mode
w.write("I deleted all of the names")
w.close()

w = open("names.txt")
print(w.read())
w.close()

#Create

x = open("created.txt", "w") #If created.txt does not exist it will create it, If it already existed open it in write mode.
x.close()
#There is another way to create a file, But that can cause error if the file already exists. So you might need to check if the file exists or not.

if not os.path.exists("created2.txt"): #This will check if the file exists or not and you have to import os module for this.
    c = open("created2.txt", "x")
    c.close()

with open("more_names.txt") as f: #This is the best way to open a file because it will automatically close the file after the indented block.
    content = f.read()

with open("test.json", "w") as w:
    w.write(content)

