boys = ['AHMAD', 'Usman', 'ALI']

girls = ['Zara', 'Jannat', 'bushra']

print(boys[1])
print(boys.index('ALI'))
for repeat in range(5):
    print(boys[0]) #This will print the first element of the list repeatedly
    print(boys[0:2]) 


girls.append("Fatima")
print(girls)

girls.remove("Fatima")
print(girls)

#the hassan.append() method adds an element to the end of the list, But if you want to add an element at a specific position, you can use the insert() method
girls.insert(1, "Fatima")
print(girls)

girls[2:2] = ['Eman', 'Maryam']  #This will insert elements at the specified position but not replace any existing elements
print(girls)  

girls[2] = ['Ayesha', 'Kainat']  #This will replace the element at index 2 with a new list
print(girls)  


del girls[0:3] #This will delete the first three elements of the list
print(girls)

girls.clear()  #This will remove all elements from the list which del does not do. Why ? Because del removes the reference to the list, while clear just empties it.
print(girls)

boys.sort()  #This will sort the list in ascending order in terms of alphabets. and lower case letters are sorted before upper case letters. even if you have logic of sorting.
print(boys)

boys[2:2] = ['hamza']
boys.sort()    #Although we added a new element, the sort method will not place hamza in the 2nd position because it is in lower case.
print(boys)

boys.remove('hamza')

boys[2:2] = ['hamza']
boys.sort(key=str.lower) #This will sort the list in ascending order in terms of alphabets, treating all letters as lower case. the key=str.lower argument is used to specify that the sorting should be done in a case-insensitive manner.
print(boys)

nums = [32, 12, 45, 67, 89, 23, 56, 78, 90]

#nums.reverse() #This will reverse the order of elements in the list
#print(nums)

#nums.sort(reverse=True) #This will sort the list in descending order
#print(nums)

#Now these methods like .sort(), reverse(), etc change the original list.

print(sorted(nums, reverse=True)) #This will return a new sorted list in descending order without changing the original list
print(nums)  #The original list remains unchanged

#There is another way to use the list without modifying the original list.

copy1_nums = nums.copy()  #This will create a copy of the original list
copy2_nums = list(nums) #This will also create a copy of the original list
copy3_nums = nums[:] #This will also create a copy of the original list


#Tuples are immutable, meaning you cannot change their elements once they are created. Nor their data Nor their order

Boys_tuple = tuple(('AHMAD', 'Usman', 'ALI', 'Talha'))
Girls_tuple = ('Zara', 'Jannat', 'bushra')

print(type(Boys_tuple))
print(type(Girls_tuple))

#Although tuples are immutable you can get creative by changing the type temporarily like:

fake_tuple = list(Boys_tuple)    
fake_tuple.append('Ahad')

print(fake_tuple)

#We can also unpack tuples and assign values of the tuples to multiple variables

(one, two, *three) = Boys_tuple

print(one)
print(two)
print(*three) #This * will take all the pending values in this one variable

print('Program successful')